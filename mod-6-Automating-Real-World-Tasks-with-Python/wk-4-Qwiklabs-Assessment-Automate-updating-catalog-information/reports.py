#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

# Desired format:
'''
Processed Update on <Today's date>

[blank line]

name: Apple
weight: 500 lbs
[blank line]
'''


def generate_report(attachment, title, paragraph):
    """Generate a pdf file with the given parameters."""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1, 20)
    elements = [report_title, empty_line]
    for item in paragraph:
        elements.append(Paragraph(item, styles["BodyText"]))
        elements.append(empty_line)
    report.build(elements)



