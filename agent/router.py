import re

from agent.analyzer import DataAnalyzer
from agent.explainer import explain


class BusinessAgent:

    def __init__(self, df):

        self.analyzer = DataAnalyzer(df)

    def answer(self, question):

        q = question.lower()

        # -----------------------------
        # Basic Questions
        # -----------------------------

        if any(word in q for word in ["row", "rows"]):
            return explain(
                self.analyzer.row_count(),
                question
            )

        if any(word in q for word in ["column", "columns"]):
            return explain(
                self.analyzer.column_count(),
                question
            )

        if "missing" in q or "null" in q:
            return explain(
                self.analyzer.missing_values(),
                question
            )

        if "duplicate" in q:
            return explain(
                self.analyzer.duplicate_rows(),
                question
            )

        # -----------------------------
        # Sales Metrics
        # -----------------------------

        if "total" in q and "sales" in q:

            result = self.analyzer.total_sales()

            if result is None:
                return "❌ Sales column not found."

            return explain(result, question)

        if "average" in q and "sales" in q:

            result = self.analyzer.average_sales()

            if result is None:
                return "❌ Sales column not found."

            return explain(result, question)

        if "total" in q and "profit" in q:

            result = self.analyzer.total_profit()

            if result is None:
                return "❌ Profit column not found."

            return explain(result, question)

        # -----------------------------
        # Generic Top Analysis
        # -----------------------------

        dimensions = [
            c
            for c in self.analyzer.df.columns
            if self.analyzer.df[c].dtype == "object"
        ]

        metric = None

        if "sales" in q:
            metric = "sales"

        elif "profit" in q:
            metric = "profit"

        if metric:

            match = re.search(r"top\s+(\d+)", q)

            top_n = int(match.group(1)) if match else 1

            for column in dimensions:

                column_lower = column.lower()

                if column_lower in q:

                    result, error = self.analyzer.group_analysis(
                        column_lower,
                        metric,
                        top_n
                    )

                    if error:
                        return error

                    return explain(result, question)

        # -----------------------------
        # Monthly Trend
        # -----------------------------

        if "monthly" in q and "sales" in q:

            result = self.analyzer.monthly_sales_trend()

            if result is None:
                return "Order Date or Sales column not found."

            return explain(result, question)

        # -----------------------------
        # Dataset Summary
        # -----------------------------

        if "summary" in q or "overview" in q:

            result = self.analyzer.dataset_summary()

            return explain(result, question)

        # -----------------------------
        # Default
        # -----------------------------

        return """
I don't understand that question yet.

Try asking:

• How many rows?
• How many columns?
• Total sales
• Average sales
• Total profit
• Top 5 customers by sales
• Top 10 products by sales
• Top category by profit
• Monthly sales trend
• Dataset summary
"""