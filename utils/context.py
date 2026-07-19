import pandas as pd


def dataset_summary(df):

    return f"""
Dataset Information

Rows: {df.shape[0]}

Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Missing Values:
{df.isnull().sum().to_string()}

Data Types:
{df.dtypes.to_string()}
"""



from utils.kpi import generate_kpis


def kpi_summary(df):

    kpis = generate_kpis(df)

    text = ""

    for key, value in kpis.items():

        text += f"{key}: {value}\n"

    return text


def statistics_summary(df):

    numeric = df.select_dtypes(include="number")

    if numeric.empty:
        return "No numeric columns."

    return numeric.describe().to_string()


def sample_data(df):

    return df.sample(
        min(15, len(df)),
        random_state=42
    ).to_string()


SYSTEM_CONTEXT = """
You are an expert Business Intelligence Consultant.

Use ONLY the supplied business information.

Never invent numbers.

If the answer is unavailable,
say so.

Always explain your reasoning.
"""



def create_context(df):

    context = f"""

{SYSTEM_CONTEXT}

======================

DATASET SUMMARY

{dataset_summary(df)}

======================

KPIs

{kpi_summary(df)}

======================

STATISTICS

{statistics_summary(df)}

======================

SAMPLE DATA

{sample_data(df)}

"""

    return context