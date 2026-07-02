from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":4,
        "fetch_k":10,
        "lambda_mult":0.5
    }
)

llm = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages([
(
"system",
"""You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found, reply:

'I could not find the answer in the document.'
"""
),

(
"human",
"""Context:

{context}

Question:

{question}
"""
)
])


def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    response = llm.invoke(
        prompt.invoke(
            {
                "context":context,
                "question":question
            }
        )
    )

    return response.content, docs