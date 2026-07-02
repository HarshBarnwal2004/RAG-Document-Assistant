import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

from create_database import create_vector_database
from rag import ask_question

st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Chat with your PDF")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Create Knowledge Base"):

        with st.spinner("Creating embeddings..."):

            create_vector_database(pdf_path)

        st.success("Knowledge base created!")

st.divider()

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    with st.spinner("Thinking..."):

        answer, docs = ask_question(question)

    st.subheader("Answer")

    st.write(answer)

    with st.expander("Retrieved Chunks"):

        for i, doc in enumerate(docs):

            st.markdown(f"### Chunk {i+1}")

            st.write(doc.page_content)