# RAG-Document-Assistant
An AI-powered Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask natural language questions about their content. The application retrieves the most relevant document chunks using semantic search and generates context-aware answers with a Large Language Model.

# Features
📄 Upload and process PDF documents
✂️ Automatic document chunking
🔍 Semantic search using vector embeddings
🧠 Retrieval-Augmented Generation (RAG)
💬 Interactive question-answering interface
⚡ Fast document retrieval with Chroma Vector Database
🤖 Powered by Mistral LLM
🌐 Streamlit-based user interface

# 🛠️ Tech Stack
Python
Streamlit
LangChain
Mistral AI
ChromaDB
Hugging Face Embeddings
PyPDF
Recursive Character Text Splitter

# 📂 Project Structure
RAG_Project/
│
├── app.py                 # Streamlit UI
├── rag.py                 # RAG backend
├── create_database.py     # PDF ingestion & vector database creation
├── chroma_db/             # Chroma vector database (generated)
├── uploads/               # Uploaded PDF files

# ⚙️ How It Works
Upload a PDF document.
The document is split into smaller chunks.
Each chunk is converted into vector embeddings using Hugging Face.
The embeddings are stored in ChromaDB.
When a user asks a question:
Relevant chunks are retrieved using semantic search.
The retrieved context is passed to the Mistral LLM.
The model generates an answer based only on the retrieved information.

# 🏗️ Architecture
                PDF Upload
                     │
                     ▼
            Document Loader
                     │
                     ▼
        Recursive Text Splitter
                     │
                     ▼
      Hugging Face Embeddings
                     │
                     ▼
             Chroma Vector DB
                     │
                     ▼
              Retriever (MMR)
                     │
                     ▼
           Retrieved Context
                     │
                     ▼
               Mistral LLM
                     │
                     ▼
              Generated Answer

# 📦 Installation

Clone the repository:

git clone https://github.com/<your-username>/RAG-Document-Assistant.git
cd RAG-Document-Assistant

Create a virtual environment:

python -m venv .venv

Activate it:

Windows

.venv\Scripts\activate

Linux/macOS

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a .env file and add your API key:

MISTRAL_API_KEY=your_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key

▶️ Run the Application

Start the Streamlit app:
streamlit run app.py

Open your browser and follow the on-screen instructions:

Upload a PDF.
Build the knowledge base.
Ask questions about the document.

├── requirements.txt
├── .env
└── README.md
