#!/usr/bin/env python3

import sys
import csv


def populate_dictionary(filename):
    """Populate a dictionary with name/email pairs for easy lookup."""
    email_dict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            name = str(row[0].lower())
            email_dict[name] = row[1]
    return email_dict


def find_email(argv):
    """ Return an email address based on the username given."""
    # Create the username based on the command line input.
    try:
        fullname = str(argv[1] + " " + argv[2])
        # Preprocess the data
        # For Google qwiklabs.com
        #email_dict = populate_dictionary('/home/student-00-78a4843906bc/data/user_emails.csv')
        # For local machine
        email_dict = populate_dictionary('user_emails.csv')
        # Find and print the email
        if email_dict.get(fullname.lower()) is not None:
            return email_dict.get(fullname.lower())
        else:
            return "No email address found"
    except IndexError:
        return "Missing parameters"


def main():
    """Get user from argv, load the emails from user_emails.csv into dictionary and search the dictionary for the
    specified user and return the user email address if found."""
    print(find_email(sys.argv))


if __name__ == "__main__":
    main()


# Usage for main:
# python3 emails.py Roy Cooper

# Output:
# "No email address found"
