import streamlit as st
from agent.router import BusinessAgent

st.title("🤖 InsightIQ AI Business Assistant")

st.write("Ask questions about your uploaded dataset.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input("Ask a question...")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Check if dataset exists
    if "df" not in st.session_state:

        answer = "⚠️ Please upload a dataset first."

    else:

        df = st.session_state["df"]

        agent = BusinessAgent(df)

        with st.spinner("Analyzing your data..."):

            try:
                answer = agent.answer(question)

            except Exception as e:
                answer = f"❌ Error: {str(e)}"

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Save chat history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )