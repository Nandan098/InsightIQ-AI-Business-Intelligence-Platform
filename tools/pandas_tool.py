import pandas as pd


class PandasTool:

    def __init__(self, df):
        self.df = df

    def row_count(self):
        return len(self.df)

    def column_count(self):
        return self.df.shape[1]

    def columns(self):
        return list(self.df.columns)

    def missing_values(self):
        return self.df.isnull().sum()

    def duplicate_rows(self):
        return self.df.duplicated().sum()

    def top_region_by_sales(self, region_col, sales_col):

        result = (
            self.df
            .groupby(region_col)[sales_col]
            .sum()
            .sort_values(ascending=False)
        )

        return {
            "region": result.index[0],
            "sales": float(result.iloc[0])
        }