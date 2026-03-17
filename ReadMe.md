# Chat with Multiple PDFs using Gemini

This project is a Streamlit application that allows users to upload
multiple PDF documents and ask questions about their contents using
Google's Gemini model.

The application extracts text from uploaded PDFs, converts the text into
vector embeddings, stores them using FAISS, and retrieves the most
relevant information when a user asks a question. The result is a simple
interface for interacting with the contents of large document
collections.

## Features

• Upload and process multiple PDF files\
• Extract and chunk document text for efficient retrieval\
• Generate embeddings using Google Generative AI\
• Store embeddings with FAISS for fast similarity search\
• Ask questions and receive answers grounded in the uploaded documents\
• Simple web interface built with Streamlit

## Installation

### Prerequisites

Make sure the following are installed:

• Python 3.8 or higher\
• pip

### Setup

Clone the repository

``` bash
git clone https://github.com/yourusername/chat-with-multiple-pdfs.git
cd chat-with-multiple-pdfs
```

Create a virtual environment (recommended)

``` bash
python -m venv venv
source venv/bin/activate
```

On Windows

``` bash
venv\Scripts\activate
```

Install dependencies

``` bash
pip install -r requirements.txt
```

Create an environment file

Create a `.env` file in the root directory and add your API key.

    GOOGLE_API_KEY=your_google_api_key_here

## Usage

Run the Streamlit application

``` bash
streamlit run app.py
```

Upload PDF files using the sidebar.

After processing the documents, enter a question related to the uploaded
PDFs and the system will retrieve relevant content and generate an
answer.

## Dependencies

This project relies on several libraries

• streamlit for the web interface\
• PyPDF2 for extracting text from PDFs\
• langchain for document processing and model orchestration\
• FAISS for vector similarity search\
• google-generativeai for Gemini model access\
• python-dotenv for environment variable management

## License

This project is released under the MIT License.

## Acknowledgments

Google Generative AI for the Gemini model\
LangChain for the AI workflow tooling\
Streamlit for the application interface
