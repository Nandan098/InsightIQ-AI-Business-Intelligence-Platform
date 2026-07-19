from langchain_ollama import ChatOllama

# Local Llama 3 model
llm = ChatOllama(
    model="llama3",
    temperature=0
)

def ask_llm(prompt: str) -> str:
    """
    Send a prompt to the local Llama 3 model.
    """
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {e}"



def get_llm():

    return ChatOllama(
        model="llama3",
        temperature=0
    )