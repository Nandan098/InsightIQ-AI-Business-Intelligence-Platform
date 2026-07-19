from llm.model import ask_llm


def explain(result, question):

    prompt = f"""
You are a Senior Business Intelligence Analyst.

Question:
{question}

Calculated Result:
{result}

Answer in this format:

Direct Answer:
Business Insight:
Recommendation:

Keep it under 120 words.
"""

    return ask_llm(prompt)