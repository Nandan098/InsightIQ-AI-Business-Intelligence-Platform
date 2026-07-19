import pandas as pd


class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    # ---------------------------------
    # Helper
    # ---------------------------------

    def _find_column(self, keyword):

        for col in self.df.columns:
            if keyword.lower() in col.lower():
                return col

        return None

    # ---------------------------------
    # Basic Analysis
    # ---------------------------------

    def row_count(self):
        return len(self.df)

    def column_count(self):
        return self.df.shape[1]

    def missing_values(self):
        return self.df.isnull().sum().to_dict()

    def duplicate_rows(self):
        return int(self.df.duplicated().sum())

    # ---------------------------------
    # Metrics
    # ---------------------------------

    def total_sales(self):

        sales = self._find_column("sales")

        if sales is None:
            return None

        return float(self.df[sales].sum())

    def average_sales(self):

        sales = self._find_column("sales")

        if sales is None:
            return None

        return float(self.df[sales].mean())

    def total_profit(self):

        profit = self._find_column("profit")

        if profit is None:
            return None

        return float(self.df[profit].sum())

    # ---------------------------------
    # Generic Group Analysis
    # ---------------------------------

    def group_analysis(self, group_keyword, metric_keyword, top_n=1):

        group_col = self._find_column(group_keyword)
        metric_col = self._find_column(metric_keyword)

        if group_col is None:
            return None, f"{group_keyword} column not found."

        if metric_col is None:
            return None, f"{metric_keyword} column not found."

        result = (
            self.df
            .groupby(group_col)[metric_col]
            .sum()
            .sort_values(ascending=False)
            .head(top_n)
        )

        return result.to_dict(), None

    # ---------------------------------
    # Monthly Trend
    # ---------------------------------

    def monthly_sales_trend(self):

        date_col = self._find_column("order date")
        sales_col = self._find_column("sales")

        if date_col is None or sales_col is None:
            return None

        df = self.df.copy()

        df[date_col] = pd.to_datetime(df[date_col])

        result = (
            df.groupby(df[date_col].dt.to_period("M"))[sales_col]
            .sum()
        )

        return result.astype(float).to_dict()

    # ---------------------------------
    # Dataset Summary
    # ---------------------------------

    def dataset_summary(self):

        return {
            "Rows": self.row_count(),
            "Columns": self.column_count(),
            "Duplicate Rows": self.duplicate_rows(),
            "Missing Values": self.missing_values(),
            "Total Sales": self.total_sales(),
            "Average Sales": self.average_sales(),
            "Total Profit": self.total_profit(),
        }