from llm.model import ask_llm


def ask_pdf(vectorstore, question):

    docs = vectorstore.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{question}

If the answer is not in the context, say:
'I couldn't find that information in the uploaded document.'
"""

    return ask_llm(prompt)