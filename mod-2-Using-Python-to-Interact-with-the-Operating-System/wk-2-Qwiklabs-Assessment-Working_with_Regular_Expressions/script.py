#!/usr/bin/env python3
import csv
import re


def contains_domain(address, domain):
    """Returns True if the email address contains the given domain,
      in the domain position, false if not."""
    domain_pattern = f'[\w\.-]+@{domain}$'
    if re.match(domain_pattern, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in
      the received address."""
    old_domain_pattern = f'{old_domain}$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


def main():
    """Processes the list of emails, replacing any instances of the
        old domain with the new domain."""
    old_domain, new_domain = 'abc.edu', 'xyz.edu'

    # For Google qwiklabs.com
    #username = 'student-00-7571184e8a4e'
    #csv_file_location = f'/home/{username}/data/user_emails.csv'
    #report_file = f'/home/{username}/data/updated_user_emails.csv'

    # For local machine
    csv_file_location = 'user_emails.csv'
    report_file = 'updated_user_emails.csv'

    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]

    for email_address in user_email_list:
        if contains_domain(email_address, old_domain):
            old_domain_email_list.append(email_address)
            replaced_email = replace_domain(
                email_address, old_domain, new_domain)
            new_domain_email_list.append(replaced_email)

    email_key = ' ' + 'Email Address'
    # get the index of the email.
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]:
        for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
            if user[email_index] == ' ' + old_domain:
                user[email_index] = ' ' + new_domain

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)

    print("\"updated_user_emails.csv\" successfully created.")

if __name__ == '__main__':
    main()
