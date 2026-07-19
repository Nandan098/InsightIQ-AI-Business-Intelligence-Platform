import pandas as pd


def clean_data(df):
    """
    Clean uploaded dataset
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing numeric values
    numeric_cols = df.select_dtypes(include=["number"]).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing categorical values
    categorical_cols = df.select_dtypes(
    include=["object", "string"]
    ).columns
   

    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Convert possible date columns
    for col in df.columns:
        if "date" in col.lower():
            try:
                df[col] = pd.to_datetime(
                df[col],
                dayfirst=True,
                errors="coerce")

            except:
                pass

    return df