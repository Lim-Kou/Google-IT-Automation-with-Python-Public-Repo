#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import HorizontalBarChart


def generate(filename, title, additional_info, table_data, total_sales_data=None, total_sales_data_description=None,
             vehicle_data=None, vehicle_data_description=None):
    """
        Generate a pdf report with the following elements:
        Report title
        Empty Line
        Report info
        Empty Line
        Report Table
        Pie Chart description (Optional)
        Empty line (Optional)
        Pie Chart (Optional)
        Horizontal bar chart description (Optional)
        Empty line (Optional)
        Empty line (Optional)
        Horizontal bar chart  (Optional)
    """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black),
                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                   ('ALIGN', (0, 0), (-1, -1), 'CENTER')]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1, 20)
    elements = [report_title, empty_line, report_info, empty_line, report_table]

    if total_sales_data:
        # Create graphics: Pie chart
        # Initialize Pie object
        report_pie = Pie()
        report_pie.x = 95
        report_pie.y = 80
        report_pie.width = 250
        report_pie.height = 250
        # To add data to our Pie chart, we need two separate lists: One for data, and one for labels.
        report_pie.data = []
        report_pie.labels = []
        for car_make in total_sales_data:
            report_pie.data.append(total_sales_data[car_make])
            report_pie.labels.append(car_make)
        # print(report_pie.data)
        # print(report_pie.labels)
        # Enable side labels
        report_pie.sideLabels = True
        # Set the side labels offset to extend their length
        report_pie.sideLabelsOffset = 0.2  # Adjust the value as needed
        # Create pie chart
        # Pie object isn’t Flowable, but it can be placed inside a Flowable Drawing.
        report_chart = Drawing(width=350, height=350)
        report_chart.add(report_pie)

        if total_sales_data_description:
            total_sales_data_description = Paragraph(total_sales_data_description, styles["h2"])
            elements.append(total_sales_data_description)
        elements.append(empty_line)
        elements.append(report_chart)

    if vehicle_data:
        # Extract the vehicle names and total sales from the data
        vehicle_names = [item[0] for item in vehicle_data]
        total_sales = [item[1] / 1000 for item in vehicle_data]

        # Create the drawing object
        drawing = Drawing(600, 200)

        # Create the horizontal bar chart
        bar_chart = HorizontalBarChart()
        bar_chart.x = 70
        bar_chart.y = 30
        bar_chart.height = 200
        bar_chart.width = 400
        bar_chart.data = [total_sales]
        bar_chart.strokeColor = colors.black
        bar_chart.fillColor = colors.white
        bar_chart.valueAxis.valueMin = 0
        bar_chart.valueAxis.valueMax = max(total_sales) + 300
        bar_chart.valueAxis.valueStep = 2500
        bar_chart.categoryAxis.labels.boxAnchor = 'ne'
        bar_chart.categoryAxis.labels.dx = -6
        bar_chart.categoryAxis.labels.dy = 7
        bar_chart.categoryAxis.labels.angle = 0  # Horizontal labels
        bar_chart.categoryAxis.tickLeft = 0  # Set tickLeft to 0 to remove the ticks
        bar_chart.categoryAxis.tickRight = 0  # Set tickRight to 0 to remove the ticks
        bar_chart.categoryAxis.categoryNames = vehicle_names

        # Add the X-axis title as a text label
        x_axis_title = "Total Revenue (K)"
        x_axis_label = String(200, 0, x_axis_title, fontName='Helvetica', fontSize=12)
        drawing.add(x_axis_label)

        # Set the fill color for each bar individually
        for i, value in enumerate(total_sales):
            bar_chart.bars[i].fillColor = colors.lightgreen  # Set the color of each bar to light green

        # Add the bar chart to the drawing
        drawing.add(bar_chart)

        # Add the bar chart to the drawing
        if vehicle_data_description:
            vehicle_data_description = Paragraph(vehicle_data_description, styles["h2"])
            elements.append(vehicle_data_description)
        elements.append(empty_line)
        elements.append(empty_line)
        elements.append(drawing)

    report.build(elements)
