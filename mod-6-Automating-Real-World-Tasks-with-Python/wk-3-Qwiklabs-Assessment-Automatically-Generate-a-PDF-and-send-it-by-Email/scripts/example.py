#!/usr/bin/env python3
import emails
import os
import reports

# This example shows how a email can be generated and sent using
# The Python emails module

table_data = [
    ['Name', 'Amount', 'Value'],
    ['elderberries', 10, 0.45],
    ['figs', 5, 3],
    ['apples', 4, 2.75],
    ['durians', 1, 25],
    ['bananas', 5, 1.99],
    ['cherries', 23, 5.80],
    ['grapes', 13, 2.48],
    ['kiwi', 4, 0.49]]

# For labs
# report_loc = "/tmp/report.pdf"
# receiver = "{}@example.com".format(os.environ.get('USER'))

# For local machine
report_loc = "tmp/report.pdf"
receiver = os.environ.get("GOOGLE_email")

reports.generate(report_loc, "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)
sender = "automation@example.com"
subject = "List of Fruits"
body = "Hi\n\nI'm sending an attachment with all my fruit."
message = emails.generate(sender, receiver, subject, body, report_loc)
emails.send(message)