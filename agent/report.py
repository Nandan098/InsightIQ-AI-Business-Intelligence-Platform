from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from agent.analyzer import DataAnalyzer
from llm.model import ask_llm


def generate_pdf_report(df):

    analyzer = DataAnalyzer(df)

    stats = analyzer.dataset_summary()

    prompt = f"""
You are a Senior Business Intelligence Consultant.

Dataset Statistics:

{stats}

Generate:

1. Executive Summary

2. Key Insights

3. Business Recommendations

Maximum 250 words.
"""

    ai_report = ask_llm(prompt)

    filename = "InsightIQ_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>InsightIQ AI Business Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph("<b>Dataset Overview</b>", styles["Heading2"])
    )

    for k,v in stats.items():

        story.append(
            Paragraph(
                f"<b>{k}</b>: {v}",
                styles["BodyText"]
            )
        )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>AI Executive Summary</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            ai_report,
            styles["BodyText"]
        )
    )

    doc.build(story)

    return filename