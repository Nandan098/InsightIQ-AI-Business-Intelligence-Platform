import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

# A toggle in the sidebar so the recruiter can see your architecture choices
RUN_MODE = st.sidebar.radio("AI Engine", ["Cloud API (Fast)", "Local Open-Source"], index=0)

def get_llm():
    if RUN_MODE == "Cloud API (Fast)":
        # 1. Securely fetch the key from Streamlit Secrets
        groq_key = st.secrets["GROQ_API_KEY"]
        os.environ["GROQ_API_KEY"] = groq_key
        
        # 2. Connect to Groq's new supported model (Replaced the decommissioned Llama 3)
        return ChatGroq(
            model="openai/gpt-oss-20b", 
            temperature=0
        )
    else:
        # 3. Fallback for your local tech interview using Phi-3 or Llama 3
        return ChatOllama(
            model="phi3", 
            temperature=0,
            client_kwargs={"timeout": 120.0}
        )
        
def ask_llm(prompt: str) -> str:
    llm = get_llm()
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {e}"