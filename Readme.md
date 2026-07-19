# 📊 InsightIQ - AI Powered Business Intelligence Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-blue)
![LangChain](https://img.shields.io/badge/LangChain-AI-green)
![Ollama](https://img.shields.io/badge/Ollama-LLM-orange)
![FAISS](https://img.shields.io/badge/FAISS-RAG-purple)

</p>

---

## 📌 Overview

InsightIQ is an AI-powered Business Intelligence platform that enables users to upload business datasets, visualize KPIs, interact with data using natural language, generate executive reports, and query PDF documents using Retrieval-Augmented Generation (RAG).

Unlike traditional dashboards, InsightIQ combines **Business Intelligence**, **Large Language Models (LLMs)**, and **Retrieval-Augmented Generation (RAG)** to provide intelligent business insights and recommendations.

---

#  Features

-  Upload CSV & Excel datasets
-  Automatic Data Cleaning
-  Interactive KPI Dashboard
-  Business Charts & Visualizations
-  AI Business Chat Assistant
-  AI Executive Summary
-  AI PDF Report Generation
-  Chat with PDF Documents (RAG)
-  Semantic Search using FAISS
-  Business Insight Recommendations

---

#  Dashboard

![Dashboard](images/dashboard.png)

The dashboard provides:

- KPI Cards
- Interactive Charts
- Business Metrics
- Dataset Overview
- Data Cleaning Summary

---

# 📈 Business Visualizations

![Charts](images/charts.png)

Interactive visualizations include:

- Sales by Region
- Sales by Category
- Monthly Sales Trend
- Profit Analysis
- Customer Analysis

---

# 🤖 AI Business Assistant

![AI Chat](images/chatbot.png)

Users can ask business questions in natural language, such as:

```
What are the total sales?

Which region generated the highest profit?

Top 10 customers by sales

Monthly sales trend

Dataset summary
```

The AI assistant performs analytics using **Pandas** and uses **Llama 3** to generate business-friendly explanations.

---

# 📄 AI Executive Report

![PDF Report](images/report.png)

Generate professional PDF reports containing:

- Dataset Overview
- KPIs
- Executive Summary
- Business Insights
- AI Recommendations

---

# 📚 Chat with PDF (RAG)

![RAG](images/rag.png)

Users can upload documents such as:

- Annual Reports
- Company Policies
- Business Documents
- Meeting Notes

and ask questions like:

```
Summarize the annual report

What are the company's risks?

What is the return policy?

Who is the CEO?
```

---

# 🏗 Project Architecture

```
                     User
                      │
                      ▼
             Upload CSV / Excel
                      │
                      ▼
               Data Loading
                      │
                      ▼
               Data Cleaning
                      │
                      ▼
          Streamlit Session State
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
     Dashboard              AI Assistant
          │                       │
          ▼                       ▼
     KPIs & Charts         Business Router
                                   │
                                   ▼
                           Pandas Analyzer
                                   │
                     ┌─────────────┴────────────┐
                     ▼                          ▼
             Business Analytics          PDF Retriever
                     │                          │
                     ▼                          ▼
                    Llama 3 AI Explainer
                              │
                              ▼
                   Business Recommendations
```

---

# 🔄 Workflow

```
Upload Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Dashboard & KPIs
        │
        ▼
AI Business Assistant
        │
        ▼
Business Analysis
        │
        ▼
AI Explanation
        │
        ▼
Executive Report
```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit |
| Language | Python |
| Data Analysis | Pandas |
| Visualization | Plotly |
| AI | Ollama + Llama 3 |
| AI Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | Sentence Transformers |
| PDF Processing | PyPDF |
| Report Generation | ReportLab |

---

# 📂 Project Structure

```
InsightIQ/
│
├── app.py
│
├── pages/
│   ├── home.py
│   ├── chatbot.py
│   └── document_chat.py
│
├── agent/
│   ├── analyzer.py
│   ├── router.py
│   ├── explainer.py
│   ├── insights.py
│   ├── summary.py
│   └── report.py
│
├── rag/
│   ├── loader.py
│   ├── vectorstore.py
│   └── retriever.py
│
├── llm/
│   └── model.py
│
├── utils/
│   ├── cleaner.py
│   ├── loader.py
│   └── visualization.py
│
├── images/
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/InsightIQ.git
```

Navigate into the project

```bash
cd InsightIQ
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Ollama

```bash
ollama run llama3
```

Start the application

```bash
streamlit run app.py
```

---

# 🎯 Future Improvements

- User Authentication
- Multi-user Workspace
- SQL Database Integration
- Cloud Deployment
- Scheduled Reports
- Power BI Connector
- Voice Assistant
- Multi-LLM Support

---

# 💡 Skills Demonstrated

- Business Intelligence
- Data Analytics
- Machine Learning
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Natural Language Processing
- Streamlit Development
- Dashboard Design
- Data Visualization
- Vector Search (FAISS)
- AI Report Generation

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Your Name**

LinkedIn: https://linkedin.com/in/your-profile

GitHub: https://github.com/your-username

Email: your@email.com