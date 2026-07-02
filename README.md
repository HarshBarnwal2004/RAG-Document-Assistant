# RAG-Document-Assistant
An AI-powered Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask natural language questions about their content. The application retrieves the most relevant document chunks using semantic search and generates context-aware answers with a Large Language Model.

## Features
📄 Upload and process PDF documents
✂️ Automatic document chunking
🔍 Semantic search using vector embeddings
🧠 Retrieval-Augmented Generation (RAG)
💬 Interactive question-answering interface
⚡ Fast document retrieval with Chroma Vector Database
🤖 Powered by Mistral LLM
🌐 Streamlit-based user interface

## 🛠️ Tech Stack
Python
Streamlit
LangChain
Mistral AI
ChromaDB
Hugging Face Embeddings
PyPDF
Recursive Character Text Splitter

## 📂 Project Structure

```text
RAG-Document-Assistant/
│
├── app.py                  # Streamlit user interface
├── rag.py                  # RAG pipeline (retrieval + LLM response generation)
├── create_database.py      # PDF processing, chunking, embeddings, and Chroma DB creation
├── chroma_db/              # Persistent Chroma vector database (generated automatically)
├── uploads/                # Uploaded PDF documents
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (API keys)
├── .gitignore              # Files and folders excluded from Git
└── README.md               # Project documentation
```


## ⚙️ How It Works

Upload a PDF document.
The document is split into smaller chunks.
Each chunk is converted into vector embeddings using Hugging Face.
The embeddings are stored in ChromaDB.
When a user asks a question:
Relevant chunks are retrieved using semantic search.
The retrieved context is passed to the Mistral LLM.
The model generates an answer based only on the retrieved information.

## 🏗️ Architecture
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


## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/HarshBarnwal2004/RAG-Document-Assistant.git
cd RAG-Document-Assistant
```

### 2. Create a Virtual Environment

```bash
uv python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root and add your API keys:

```env
MISTRAL_API_KEY=your_mistral_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Once the application launches in your browser:

1. 📄 Upload a PDF document.
2. 🧠 Build the knowledge base by generating embeddings.
3. 💬 Ask questions about the uploaded document.
4. 🤖 Receive context-aware answers generated using the RAG pipeline.

---

## 📌 Example Workflow

```text
Upload PDF
      │
      ▼
Create Vector Database
      │
      ▼
Ask a Question
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Generate Answer with Mistral AI
```

## screenshots

<img width="1211" height="712" alt="image" src="https://github.com/user-attachments/assets/05ff6ab7-5925-4211-b46e-cef8d31f6b9a" />
<img width="1825" height="765" alt="Screenshot 2026-07-03 005306" src="https://github.com/user-attachments/assets/69b31402-70d0-4fb6-a1bc-878a575da6e1" />
<img width="1211" height="712" alt="Screenshot 2026-07-03 005335" src="https://github.com/user-attachments/assets/cc197c35-b70f-4052-96a9-e0e4ce98e62e" />



