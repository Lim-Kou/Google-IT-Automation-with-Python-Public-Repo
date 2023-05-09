#!/usr/bin/env python3

import re
import operator
import csv
import subprocess


def csv_to_html(script_path, csvname_path, htmlname_path):
    """Converts CSV file to html file."""
    subprocess.run([script_path, csvname_path, htmlname_path])
    print()


def main():
    """Open syslog.log file, split data into "user_statistics.csv" and "error_message.csv". Convert
    "user_statistics.csv" into "user_statistics.html" and "error_message.csv" to "error_message.html"."""
    error = {}
    per_user = {}
    # For Google qwiklabs.com
    # with open('syslog.log', 'r') as file:
    with open(
            'syslog.log', 'r') as file:
        lines = file.readlines()

    line_counter = 0

    for line in lines:
        line = line.strip()
        match = re.search(r"ticky: (INFO|ERROR) ([\w\s']*) [\[#0-9\] ]*\(([\w.]+)\)$", line)
        line_counter += 1
        if match is None:
            raise ValueError("Re did not find a match at line " + str(line_counter) + ": " + line)
        matched_text = match.groups()
        user_error = matched_text[0]
        message = matched_text[1]
        user = matched_text[2]
        if user not in per_user.keys():
            per_user[user] = [0, 0]
        if user_error == "ERROR":
            if message not in error.keys():
                error[message] = 0
        if user_error == "INFO":
            per_user[user][0] += 1
        else:
            per_user[user][1] += 1
            error[message] += 1

    # Sort per_user
    per_user = sorted(per_user.items(), key=operator.itemgetter(0))

    # Sort error
    error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

    # convert per_user into csv_format to write to csv_file
    with open(
            "user_statistics.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'INFO', 'ERROR'])
        for line in per_user:
            writer.writerow([line[0], line[1][0], line[1][1]])
    print("\nuser_statistics.csv successfully created")

    # covert error into csv_format to write to csv_file
    with open(
            "error_message.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['ERROR', 'COUNT'])
        for line in error:
            writer.writerow([line[0], line[1]])
    print("error_message.csv successfully created \n")

    # Convert user_statistics.csv to user_statistics.html file
    # csv_to_html(r"./csv_to_html.py", r"./user_statistics.csv", r"/var/www/html/user_statistics.html")
    csv_to_html(r"./csv_to_html.py", r"user_statistics.csv", r"user_statistics.html")

    # Convert error_message.csv to error_message.html file
    # csv_to_html(r"./csv_to_html.py", r"./error_message.csv", r"/var/www/html/error_message.csv.html")
    csv_to_html(r"./csv_to_html.py", r"error_message.csv", r"error_message.html")


if __name__ == "__main__":
    main()
