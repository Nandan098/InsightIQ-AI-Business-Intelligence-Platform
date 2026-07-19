import streamlit as st

from rag.loader import load_pdf
from rag.vectorstore import build_vectorstore
from rag.retriever import ask_pdf

st.title("📄 Chat with PDF")

pdf = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if pdf:

    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    docs = load_pdf("temp.pdf")

    vectorstore = build_vectorstore(docs)

    question = st.chat_input("Ask about the document")

    if question:

        with st.spinner("Searching..."):

            answer = ask_pdf(
                vectorstore,
                question
            )

        st.write(answer)