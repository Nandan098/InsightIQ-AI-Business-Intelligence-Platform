import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file):
    file_name = file.name.lower() 
    
    if file_name.endswith(".csv"):
        df = pd.read_csv(file)
    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")

    return df