import streamlit as st
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="PDF AI Chatbot", page_icon="📄")

st.title("📄 Chat with your PDF")
st.write("Upload a PDF and ask questions!")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# Session state
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================
# 📄 PROCESS PDF (WITH LOADER)
# =========================
if uploaded_file is not None:

    progress = st.progress(0)
    status_text = st.empty()

    # Step 1: Save + Load PDF
    status_text.text("📄 Reading PDF...")
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()
    progress.progress(25)

    # Step 2: Split
    status_text.text("✂️ Splitting document...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(docs)
    progress.progress(50)

    # Step 3: Embeddings
    status_text.text("🧠 Creating embeddings...")
    embedding_model = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    progress.progress(75)

    # Step 4: Store in Chroma
    status_text.text("📦 Storing in vector database...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )
    progress.progress(100)

    st.session_state.vectorstore = vectorstore

    status_text.text("✅ Done! You can now ask questions.")
# =========================
# 💬 ASK QUESTION WITH BUTTON
# =========================

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask a question from your PDF")
    submit_button = st.form_submit_button("🚀 Ask")

if submit_button and user_input and st.session_state.vectorstore:

    with st.spinner("🔍 Searching relevant content..."):
        retriever = st.session_state.vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 4, "fetch_k": 10, "lambda_mult": 0.5}
        )

        docs = retriever.invoke(user_input)
        context = "\n".join([doc.page_content for doc in docs])

    with st.spinner("🤖 Generating answer..."):
        llm = ChatMistralAI(model="mistral-small-2506")

        prompt = ChatPromptTemplate.from_messages([
            ("system",
             "You are a helpful assistant. Answer only from the given context."),
            ("human",
             "Context:\n{context}\n\nQuestion: {question}")
        ])

        final_prompt = prompt.invoke({
            "context": context,
            "question": user_input
        })

        response = llm.invoke(final_prompt)

    # Save chat
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", response.content))
# =========================
# 💬 CHAT HISTORY DISPLAY
# =========================
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **AI:** {msg}")