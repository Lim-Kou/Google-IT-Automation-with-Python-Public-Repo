# This is a practice file that contains codes from Coursera.

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.pagesizes import inch


fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

# Create tables
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])
print(table_data)

# Create graphics: Pie chart
# Initialize Pie object
report_pie = Pie(width=3 * inch, height=3 * inch)
# To add data to our Pie chart, we need two separate lists: One for data, and one for labels.
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
print(report_pie.data)
print(report_pie.labels)
# Enable side labels
report_pie.sideLabels = True


# Build pdf
report = SimpleDocTemplate("report.pdf")
# Import style
styles = getSampleStyleSheet()
# report title
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
# Add tables
report_table = Table(data=table_data)
# Add boarder to tables
table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
# Create pie chart
# Pie object isn’t Flowable, but it can be placed inside a Flowable Drawing.
report_chart = Drawing()
report_chart.add(report_pie)

# Build report
report.build([report_title, report_table, report_chart])
