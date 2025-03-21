# 📄 Chat with Multiple PDFs using Gemini

This project is a **Streamlit-based application** that enables users to **upload multiple PDF files** and interact with them using **Google's Gemini AI model**. The app extracts text from PDFs, processes it into vector embeddings using FAISS, and allows users to ask questions based on the content of the uploaded documents.

## 🚀 Features

- ✅ **Upload multiple PDF files**
- ✅ **Extract and split text for efficient processing**
- ✅ **Convert text into embeddings using Google's Generative AI**
- ✅ **Store and retrieve information using FAISS (Facebook AI Similarity Search)**
- ✅ **Chat with your PDFs using a conversational AI model**
- ✅ **Intuitive web interface built with Streamlit**

## 🛠 Installation

### 📌 Prerequisites

Ensure you have the following installed:

- 🐍 Python 3.8+
- 📦 pip

### 📥 Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/chat-with-multiple-pdfs.git
   cd chat-with-multiple-pdfs
   ```

2. **Create a virtual environment** _(optional but recommended)_:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory and add:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```
   - Replace `your_google_api_key_here` with your actual API key.

## 🎯 Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Upload PDFs**:
   - Use the **sidebar** to upload multiple PDF files.
   - Click the `Submit and Process` button to process the documents.

3. **Ask Questions**:
   - Enter a question related to the uploaded PDFs.
   - The AI model will retrieve relevant information and respond.

## 📦 Dependencies

This project uses the following libraries:

- 🖥 `streamlit` - for building the web application.
- 📄 `PyPDF2` - for extracting text from PDFs.
- 🧠 `langchain` - for processing and managing AI interactions.
- ⚡ `FAISS` - for efficient text retrieval.
- 🤖 `google-generativeai` - for AI-powered responses.
- 🔐 `dotenv` - for managing environment variables.

## 📜 License

This project is licensed under the **MIT License**.

## 🙌 Acknowledgments

- 💡 **Google Generative AI** for powering the chatbot.
- 🔗 **LangChain** for seamless integration of AI models.
- 🎨 **Streamlit** for an easy-to-use UI framework.

---

💡 *Feel free to modify and improve the project as needed!* 🚀
