from langchain.tools import tool

TOOL_DF = None


def set_dataframe(df):
    global TOOL_DF
    TOOL_DF = df


@tool
def row_count():

    """Return the number of rows."""

    return len(TOOL_DF)


@tool
def column_count():

    """Return the number of columns."""

    return TOOL_DF.shape[1]