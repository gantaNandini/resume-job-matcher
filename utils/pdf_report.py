from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import os
import time

def generate_pdf(score, confidence, section_scores, skill_gap, reasons):
    os.makedirs("static/reports", exist_ok=True)

    filename = f"resume_report_{int(time.time())}.pdf"
    file_path = f"static/reports/{filename}"

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("<b>Resume–Job Match Report</b>", styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"<b>Overall Match Score:</b> {score}%", styles["Normal"]))
    content.append(Paragraph(f"<b>Confidence Level:</b> {confidence}", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("<b>Section-wise Scores</b>", styles["Heading2"]))
    for sec, sc in section_scores.items():
        content.append(Paragraph(f"{sec}: {sc}%", styles["Normal"]))

    content.append(Spacer(1, 12))

    content.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))
    for s in skill_gap["missing"]:
        content.append(Paragraph(f"- {s}", styles["Normal"]))

    content.append(Spacer(1, 12))

    content.append(Paragraph("<b>Why the Score Is Low</b>", styles["Heading2"]))
    for r in reasons:
        content.append(Paragraph(f"- {r}", styles["Normal"]))

    doc.build(content)
    return file_path
