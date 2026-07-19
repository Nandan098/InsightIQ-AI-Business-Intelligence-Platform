def detect_column(df, keywords):
    """
    Detect a column whose name matches one of the keywords.
    """

    for col in df.columns:

        col_name = col.lower()

        for keyword in keywords:

            if keyword in col_name:
                return col

    return None


def detect_columns(df):
    """
    Detect commonly used business columns.
    """

    return {

        "sales": detect_column(df, ["sales", "revenue", "amount"]),

        "profit": detect_column(df, ["profit"]),

        "date": detect_column(df, ["date"]),

        "region": detect_column(df, ["region", "state"]),

        "category": detect_column(df, ["category"]),

        "customer": detect_column(df, ["customer"]),

        "order": detect_column(df, ["order"])

    }


def generate_kpis(df):
    """
    Generate dynamic KPIs based on detected columns.
    """

    columns = detect_columns(df)

    kpis = {}

    if columns["sales"]:
        kpis["Revenue"] = round(df[columns["sales"]].sum(), 2)

    if columns["profit"]:
        kpis["Profit"] = round(df[columns["profit"]].sum(), 2)

    if columns["customer"]:
        kpis["Customers"] = df[columns["customer"]].nunique()

    if columns["order"]:
        kpis["Orders"] = df[columns["order"]].nunique()

    return kpis