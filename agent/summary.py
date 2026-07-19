from agent.analyzer import DataAnalyzer
from llm.model import ask_llm


def generate_summary(df):

    analyzer = DataAnalyzer(df)

    info = {
        "Rows": analyzer.row_count(),
        "Columns": analyzer.column_count(),
        "Duplicate Rows": analyzer.duplicate_rows(),
        "Missing Values": analyzer.missing_values(),
        "Top Region": analyzer.top_region_by_sales()
    }

    prompt = f"""
You are a Senior Business Intelligence Consultant.

Using the following dataset statistics:

{info}

Generate a professional report with:

1. Dataset Overview
2. Key Insights
3. Business Recommendations

Keep it under 250 words.
"""

    return ask_llm(prompt)