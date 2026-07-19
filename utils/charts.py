import plotly.express as px
import pandas as pd


def sales_trend(df, date_col, sales_col):

    data = df.groupby(date_col)[sales_col].sum().reset_index()

    fig = px.line(
        data,
        x=date_col,
        y=sales_col,
        title="Sales Trend"
    )

    return fig


def region_sales(df, region_col, sales_col):

    data = df.groupby(region_col)[sales_col].sum().reset_index()

    fig = px.bar(
        data,
        x=region_col,
        y=sales_col,
        title="Sales by Region"
    )

    return fig



def category_sales(df, category_col, sales_col):

    data = df.groupby(category_col)[sales_col].sum().reset_index()

    fig = px.pie(
        data,
        names=category_col,
        values=sales_col,
        title="Sales by Category"
    )

    return fig


def profit_distribution(df, profit_col):

    fig = px.histogram(
        df,
        x=profit_col,
        title="Profit Distribution"
    )

    return fig



