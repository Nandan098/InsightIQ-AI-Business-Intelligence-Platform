import pandas as pd


class BusinessAgent:

    def __init__(self, df):
        self.df = df

    def answer(self, question: str):

        q = question.lower()

        # ------------------------
        # Dataset Information
        # ------------------------

        if "row" in q:
            return f"The dataset contains {len(self.df):,} rows."

        if "column" in q:
            return (
                f"The dataset contains {self.df.shape[1]} columns.\n\n"
                + ", ".join(self.df.columns)
            )

        if "missing" in q:
            missing = self.df.isnull().sum()

            report = missing[missing > 0]

            if report.empty:
                return "There are no missing values in the dataset."

            text = "Missing values by column:\n\n"

            for col, value in report.items():
                text += f"- {col}: {value}\n"

            return text

        if "duplicate" in q:
            dup = self.df.duplicated().sum()
            return f"There are {dup:,} duplicate rows."

        # ------------------------
        # Region with Highest Sales
        # ------------------------

        if (
            "region" in q
            and "sales" in q
            and (
                "highest" in q
                or "top" in q
                or "maximum" in q
                or "most" in q
            )
        ):

            sales_col = None
            region_col = None

            for col in self.df.columns:

                if "sales" in col.lower():
                    sales_col = col

                if "region" in col.lower():
                    region_col = col

            if sales_col is None or region_col is None:
                return "Sales or Region column not found."

            result = (
                self.df
                .groupby(region_col)[sales_col]
                .sum()
                .sort_values(ascending=False)
            )

            best_region = result.index[0]
            sales = result.iloc[0]

            return (
                f"The region with the highest sales is "
                f"**{best_region}** "
                f"with total sales of **{sales:,.2f}**."
            )

        return None