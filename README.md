## Chat with Your Data 📊💬

A Streamlit-powered app to interact with your CSV, Excel, and SQL data using AI-based natural language queries. Upload your data, ask questions, and get insights—all in an easy-to-use chat interface!

🚀 Live App
Try the live version on Streamlit (https://chatwithdatacsv.streamlit.app/)

📂 GitHub Repository
GitHub Repository Link

Overview

Chat with Your Data is a powerful tool that allows you to interact with datasets by asking questions in plain English. Leveraging the Google Generative AI API, this app can answer questions, generate summaries, and provide insights into data uploaded in CSV, Excel, or SQL format.

Whether you’re analyzing large datasets, exploring trends, or generating reports, this app enables you to retrieve insights without needing SQL or coding skills. Additionally, the app allows you to save your chat history as a downloadable PDF.








## Features

Data Support: Easily upload and query data in CSV, Excel, or SQL formats.

AI-Powered Chat: Powered by Google's Generative AI, enabling natural language interactions with your data.
Streamlined Analysis: Get instant responses to complex data questions.

PDF Export: Save your chat history as a PDF for easy reference and sharing.

User-Friendly Interface: Clean, intuitive interface using Streamlit.





## ```Advantages
No Coding Required: Ask questions in natural language, and get answers directly from your data.

Multiple Data Formats: Supports CSV, Excel, and SQL for versatile data handling.

On-the-Fly Analysis: Instantly analyze data without requiring database querying skills
.
Portable Results: Export chat history to PDF, making it easier to document insights and share with others.



## Getting Started

1. Using the Online App


Visit the Streamlit app link(https://chatwithdatacsv.streamlit.app/) to use the app directly in your browser. Upload your dataset, type your questions, and start interacting with the data right away!




## To run this application locally, follow these steps:



Clone the project

```bash
  git clone https://github.com/REASCREH/csv-chat.git




```

Go to the project directory

```bash
  cd csv-chat


```

Install dependencies

```bash
  pip install -r requirements.txt
  GOOGLE_API_KEY="your_google_api_key_here"


```


Start the server

```bash
  streamlit run csvapp.py


```


Usage

Upload Data: After starting the app, upload your CSV, Excel, or SQL file.

Ask Questions: Enter questions about your data in the input box.

View Responses: The AI agent will analyze the data and provide answers.

Export to PDF: Download your chat history as a PDF for documentation or sharing purposes.

## How It Works


Data Processing: The app reads uploaded data (CSV, Excel, or SQL) and processes it with Pandas.

LLM Integration: Your queries are sent to the Google Generative AI model for natural language processing.

CSV Agent: The LangChain library creates a CSV agent that allows the AI to interact with data, parse queries, and handle responses effectively.

PDF Generation: Chat history is saved as a PDF using the FPDF library.
