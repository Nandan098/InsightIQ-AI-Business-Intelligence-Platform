import streamlit as st
from utils.loader import load_data
from utils.cleaner import clean_data
from utils.kpi import detect_columns, generate_kpis
from utils.charts import (
    sales_trend,
    region_sales,
    category_sales,
    profit_distribution,
)
from agent.report import generate_pdf_report
import pandas as pd
import plotly.express as px

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
         InsightIQ
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
###  Turn Business Data into Actionable Insights

InsightIQ enables you to:

-  Upload CSV or Excel datasets
-  Automatically clean data
-  Visualize KPIs and dashboards
-  Chat with your business data
-  Generate AI business insights
-  Create Executive PDF reports
-  Chat with PDF documents using RAG

Everything in one place.
"""
)

st.markdown("---")

# --------------------------
# Workflow
# --------------------------

st.subheader("Workflow")

st.info("**Upload Dataset** ➡ **Data Cleaning** ➡ **Interactive Dashboard** ➡ **AI Business Assistant** ➡ **Business Insights** ➡ **Executive Report**")
st.markdown("---")

# --------------------------
# Features
# --------------------------

st.subheader(" Key Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.success(" Smart Data Upload")

    st.write("""
- CSV Support
- Excel Support
- Automatic Loading
""")

    st.success("Data Cleaning")

    st.write("""
- Missing Value Detection
- Duplicate Detection
- Data Quality Checks
""")

with col2:

    st.success("Dashboard")

    st.write("""
- KPIs
- Interactive Charts
- Business Metrics
""")

    st.success("AI Assistant")

    st.write("""
- Natural Language Queries
- Business Explanations
- Data Analysis
""")

with col3:

    st.success("AI Reports")

    st.write("""
- Executive Summary
- PDF Export
- AI Recommendations
""")

    st.success("RAG")

    st.write("""
- Chat with PDFs
- Semantic Search
- FAISS Vector Store
""")


with st.sidebar:
    st.title("📊 InsightIQ")
    st.caption("AI-Powered Business Intelligence")
    st.divider()

    st.subheader("Project Status")
    st.success("✅ Upload")
    st.success("✅ Cleaning")
    st.success("✅ Dashboard")
    st.warning("🚧 AI Chat")
    st.warning("🚧 Executive Report")
    st.divider()

    if "df" in st.session_state:
        st.metric(
            "Rows",
            f"{st.session_state['df'].shape[0]:,}"
        )
        st.metric(
            "Columns",
            st.session_state["df"].shape[1]
        )
    else:
        st.error("No dataset loaded")

    st.divider()
    st.caption("InsightIQ v1.0")

st.title("📊 InsightIQ")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)

if uploaded_file:
    df = load_data(uploaded_file)
    df = clean_data(df)
    st.session_state["df"] = df

    st.success("Dataset Loaded Successfully")
    st.dataframe(df.head())

    st.markdown("## Dataset Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", f"{df.shape[0]:,}")

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", f"{df.isnull().sum().sum():,}")

    with col4:
        st.metric("Duplicate Rows", f"{df.duplicated().sum():,}")

    # Generate KPIs
    kpis = generate_kpis(df)

    st.markdown("## Business KPIs")

    cols = st.columns(len(kpis))

    for i, (key, value) in enumerate(kpis.items()):
        cols[i].metric(key, value)

    columns = detect_columns(df)
    st.markdown("## Business Dashboard")


    # region chart

    if columns["date"] and columns["sales"]:
        date_col = columns["date"]
        sales_col = columns["sales"]
    
        # Create a copy to avoid altering your original dataframe
        temp_df = df.copy()
    
        # 1. Ensure the date column is in datetime format
        temp_df[date_col] = pd.to_datetime(temp_df[date_col])
    
        # 2. Extract the month (Formatting as 'YYYY-MM' keeps chronological order correct)
        temp_df['Month'] = temp_df[date_col].dt.strftime('%m')
    
        # 3. Group by the new 'Month' column and calculate the sum of sales
        monthly_sales = temp_df.groupby('Month')[sales_col].sum().reset_index()
    
        # 4. Create the line chart
        fig = px.line(
            monthly_sales, 
            x='Month', 
            y=sales_col, 
            title="Monthly Sales Trend",
            markers=True # Adds dots to the line for each month
        )
    
        # 5. Display in Streamlit
        st.plotly_chart(fig, use_container_width=True)

    if columns["category"] and columns["sales"]:
        category_col = columns["category"]
        sales_col = columns["sales"]
    
        # 1. Group by category and calculate the sum of sales
        category_sales_df = df.groupby(category_col)[sales_col].sum().reset_index()
    
        # 2. Sort the values in descending order for a cleaner bar chart
        category_sales_df = category_sales_df.sort_values(by=sales_col, ascending=False)
    
        # 3. Create the bar chart
        fig = px.bar(
            category_sales_df, 
            x=category_col, 
            y=sales_col, 
            title="Total Sales by Category",
            text_auto='.2s' # This automatically adds shortened labels (e.g., 1.5M, 20k) to the bars
        )
    
        # 4. Display in Streamlit
        st.plotly_chart(fig, use_container_width=True)


    if columns["profit"]:
        profit_col = columns["profit"]
        
        # Create a histogram to show the distribution of profits
        fig = px.histogram(
            df, 
            x=profit_col, 
            title="Profit Distribution",
            nbins=50,             # Adjusts the number of bars for better granularity
            marginal="box"        # Adds a small box plot at the top to highlight outliers and the median
        )
        
        # Display in Streamlit
        st.plotly_chart(fig, use_container_width=True)

    categorical_columns = df.select_dtypes(include="object").columns

    selected_filters = {}

    for column in categorical_columns:
        values = st.sidebar.multiselect(
            column,
            df[column].unique(),
            default=df[column].unique()
        )
        selected_filters[column] = values

    filtered_df = df.copy()

    for column, values in selected_filters.items():
        filtered_df = filtered_df[
            filtered_df[column].isin(values)
        ]

    from agent.summary import generate_summary

    if st.button("Generate AI Executive Summary"):
        with st.spinner("Generating report..."):
            summary = generate_summary(df)

        st.subheader("Executive Summary")
        st.write(summary)

    st.divider()

    st.subheader("AI Report")

    if st.button("Generate PDF Report"):
        with st.spinner("Generating report..."):
            pdf = generate_pdf_report(df)

        with open(pdf, "rb") as file:
            st.download_button(
                "⬇ Download Report",
                file,
                file_name=pdf,
                mime="application/pdf"
            )