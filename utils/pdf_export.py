from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import re


def clean_text(text):

    text = str(text)

    # Remove markdown headings
    text = re.sub(r'#+\s*', '', text)

    # Remove bold/italic markers
    text = text.replace("**", "")
    text = text.replace("*", "")

    # Remove backticks
    text = text.replace("```", "")
    text = text.replace("`", "")

    # Normalize spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

def create_pdf_report(result, output_path):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "CivicLens AI Report",
            styles["Title"]
        )
    )
    content.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            "Summary",
            styles["Heading2"]
        )
    )

    summary_text = clean_text(result["summary"])

    content.append(
        Paragraph(
            summary_text,
            styles["BodyText"]
        )
    )
    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Dates",
            styles["Heading2"]
        )
    )

    for d in result["dates"]:

        content.append(
            Paragraph(
                f"• {d}",
                styles["BodyText"]
            )
        )


    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Eligibility",
            styles["Heading2"]
        )
    )

    if isinstance(result["eligibility"], dict):

        for key, value in result["eligibility"].items():

            content.append(
                Paragraph(
                    f"<b>{key.title()}</b>",
                    styles["Heading3"]
                )
            )

            if isinstance(value, list):

                for item in value:

                    content.append(
                        Paragraph(
                            f"• {item}",
                            styles["BodyText"]
                        )
                    )
    

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Action Plan",
            styles["Heading2"]
        )
    )

    for step in clean_text(result["action_plan"]).split("\n"):
        step = step.strip()

        if step:

            content.append(
                Paragraph(
                    f"• {step}",
                    styles["BodyText"]
                )
            )
    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            "Statistics",
            styles["Heading2"]
        )
    )

    stats = f"""
    Characters: {len(result['summary'])}<br/>
    Words: {len(result['summary'].split())}<br/>
    Dates Found: {len(result['dates'])}
    """

    content.append(
        Paragraph(
            stats,
            styles["BodyText"]
        )
    )

    doc.build(content)