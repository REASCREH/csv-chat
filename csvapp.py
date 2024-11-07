import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_csv_agent
import pandas as pd
import os
from fpdf import FPDF
from sqlalchemy import create_engine

# Ensure the Google API Key is set in the environment (set securely before deployment)
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")  # Ensure this is set securely in deployment

# Define PDF class for chat history export
class PDF(FPDF): 
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Chat History', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def main():
    st.title("Chat with Your Data")

    # Step 1: File Upload
    uploaded_file = st.file_uploader("Upload a file (Excel, CSV, or SQL)", type=["csv", "xlsx", "xls", "sql"])
    if uploaded_file is not None:
        # Convert Excel or SQL to CSV
        if uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.sql'):
            # Connect to a SQL database
            database_url = st.text_input("Enter your database URL (e.g., sqlite:///yourdb.db)")
            if database_url:
                engine = create_engine(database_url)
                table_name = st.text_input("Enter the table name:")
                if table_name:
                    df = pd.read_sql_table(table_name, con=engine)
                else:
                    st.write("Please enter the table name.")
                    return
            else:
                st.write("Please enter the database URL.")
                return
        else:  # CSV
            df = pd.read_csv(uploaded_file)

        st.write("File loaded successfully!")

        # Save the DataFrame to CSV
        df.to_csv("temp_uploaded_file.csv", index=False)
        
        # Step 2: Initialize LLM with Google API Key
        llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=os.environ["GOOGLE_API_KEY"])

        # Step 3: Create CSV Agent
        agent = create_csv_agent(
            llm,
            "temp_uploaded_file.csv",
            verbose=True,
            allow_dangerous_code=True,
            handle_parsing_errors=True
        )

        # Step 4: Chat Input
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        st.write("Ask any question about the uploaded data:")
        user_input = st.text_input("Your question:")

        if user_input:
            try:
                response = agent.run(user_input)
                # Append user and agent responses to chat history
                st.session_state.chat_history.append(f"You: {user_input}")
                st.session_state.chat_history.append(f"Agent: {response}")

                # Display chat history
                for chat in st.session_state.chat_history:
                    st.write(chat)
            except Exception as e:
                st.write("An error occurred:", str(e))

        # Step 5: PDF Generation
        if st.button("Download Chat as PDF"):
            pdf = PDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Add all chat messages to the PDF
            for chat in st.session_state.chat_history:
                pdf.multi_cell(0, 10, chat)

            # Save PDF and provide download link
            pdf_file_path = "chat_history.pdf"
            pdf.output(pdf_file_path)

            with open(pdf_file_path, "rb") as f:
                st.download_button(
                    label="Download PDF",
                    data=f,
                    file_name=pdf_file_path,
                    mime="application/pdf"
                )

if __name__ == "__main__":
    main()
