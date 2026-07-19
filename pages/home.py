import streamlit as st

st.set_page_config(
    page_title="InsightIQ",
    page_icon="📊",
    layout="wide"
)

# --------------------------
# Header
# --------------------------

st.markdown(
    """
    <h1 style='text-align:center;color:#1f77b4;'>
        📊 InsightIQ
    </h1>

    <h3 style='text-align:center;color:gray;'>
        AI Powered Business Intelligence Platform
    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown(
"""
### 🚀 Turn Business Data into Actionable Insights

InsightIQ enables you to:

- 📂 Upload CSV or Excel datasets
- 🧹 Automatically clean data
- 📈 Visualize KPIs and dashboards
- 🤖 Chat with your business data
- 🧠 Generate AI business insights
- 📄 Create Executive PDF reports
- 📚 Chat with PDF documents using RAG

Everything in one place.
"""
)

st.markdown("---")

# --------------------------
# Workflow
# --------------------------

st.subheader("⚙️ Workflow")

st.info(
"""
Upload Dataset

⬇

Data Cleaning

⬇

Interactive Dashboard

⬇

AI Business Assistant

⬇

Business Insights

⬇

Executive Report
"""
)

st.markdown("---")

# --------------------------
# Features
# --------------------------

st.subheader("✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("📂 Smart Data Upload")

    st.write("""
- CSV Support
- Excel Support
- Automatic Loading
""")

    st.success("🧹 Data Cleaning")

    st.write("""
- Missing Value Detection
- Duplicate Detection
- Data Quality Checks
""")

with col2:

    st.success("📊 Dashboard")

    st.write("""
- KPIs
- Interactive Charts
- Business Metrics
""")

    st.success("🤖 AI Assistant")

    st.write("""
- Natural Language Queries
- Business Explanations
- Data Analysis
""")

with col3:

    st.success("📄 AI Reports")

    st.write("""
- Executive Summary
- PDF Export
- AI Recommendations
""")

    st.success("📚 RAG")

    st.write("""
- Chat with PDFs
- Semantic Search
- FAISS Vector Store
""")

st.markdown("---")

# --------------------------
# Technology
# --------------------------

st.subheader("🛠 Tech Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.metric("Frontend", "Streamlit")

tech2.metric("Visualization", "Plotly")

tech3.metric("AI", "Llama 3 + Ollama")

tech4.metric("Framework", "LangChain")

st.markdown("---")

# --------------------------
# Architecture
# --------------------------

st.subheader("🏗 Architecture")

st.code(
"""
User
 │
 ▼
Upload Dataset
 │
 ▼
Data Cleaning
 │
 ▼
Dashboard + KPIs
 │
 ├─────────────┐
 ▼             ▼
AI Chat      AI Insights
 │             │
 ▼             ▼
Business Router
 │
 ▼
Pandas Analyzer
 │
 ▼
Llama 3
 │
 ▼
Executive Report
""",
language="text"
)

st.markdown("---")

# --------------------------
# Footer
# --------------------------

st.markdown(
"""
<div style='text-align:center'>

### 💡 InsightIQ

AI Powered Business Intelligence Platform

Built with ❤️ using

Python • Streamlit • Pandas • Plotly • LangChain • Ollama • Llama 3 • FAISS

</div>
""",
unsafe_allow_html=True
)