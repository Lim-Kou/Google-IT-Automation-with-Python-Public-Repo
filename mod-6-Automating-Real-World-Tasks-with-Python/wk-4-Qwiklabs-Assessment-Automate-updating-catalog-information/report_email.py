#!/usr/bin/env python3

import os
import reports
import emails
from datetime import date


def phrase_data(path):
    """
        Given a directory path, return a list of lists: where each list is in the given format:
        name: Apple
        weight: 500 lbs
    """

    def extract_lines(infile_path):
        """Given a file path, return a list of containing values for: name and weight."""
        if infile_path.endswith("txt"):
            # Open the text file
            with open(infile_path, 'r') as file:
                lines = file.read().splitlines()[:2]
                lines = [line for line in lines if line.strip()]
            return lines

    def phrase_string(item):
        """
            Given a list containing: name and weight, return a string in the given format:
            name: Apple
            weight: 500 lbs
        """
        return "name: {}<br/>weight: {}".format(item[0], item[1])

    paragraph_list = []
    for infile in sorted(os.listdir(path)):
        infile_path = os.path.join(path, infile)
        formatted_string = phrase_string(extract_lines(infile_path))
        paragraph_list.append(formatted_string)
    return paragraph_list


def main():
    """Generate a pdf attachment, before attaching it to an email and sending the email out."""
    # For Lab
    # username = "student-03-dbb2c0876961"
    # recipient = "{}@example.com".format(username)
    # attachment_path = "/tmp/processed.pdf"
    # For local machine
    recipient = os.environ.get("GOOGLE_email")
    attachment_path = "tmp/processed.pdf"
    # get today date
    today_date = date.today().strftime("%B %d, %Y")
    # Generate pdf attachment
    title = "Processed Update on {}".format(today_date)
    paragraph_list = phrase_data(path="supplier-data/descriptions")
    reports.generate_report(attachment=attachment_path, title=title, paragraph=paragraph_list)
    # generate email
    email = emails.generate_email(sender="automation@example.com", recipient=recipient,
                                  subject="Upload Completed - Online Fruit Store",
                                  body="All fruits are uploaded to our website successfully. A detailed list is "
                                       "attached to this email.", attachment_path=attachment_path)
    # Send email
    emails.send_email(email)


if __name__ == '__main__':
    main()
