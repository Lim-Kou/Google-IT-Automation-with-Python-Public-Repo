#!/usr/bin/env python3
import csv
import os.path

def read_employees(csv_file_location):
    """Return a list of dictionaries, with each dictionary containing the employees data when given an Excel data
    source. Each dictionary contains the employee full name, username and department."""
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(
        open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list


def process_data(employee_lists):
    """Returns a dictionary with the department as the key and the number of employees in the department as the
    value."""
    department_list = []
    for employee_data in employee_lists:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(
            department_name)
    return department_data


def write_report(dict, report_file):
    """Write a dictionary to a specified text file."""
    with open(report_file, "w+") as f:
        for k in sorted(dict):
            f.write(str(k) + ':' + str(dict[k]) + '\n')
        f.close()


def main():
    """ Extract data from csv file to a list, extract required data from the list and write it into a specified text
    file"""
    # Extract data from csv file.
    employee_list = read_employees('employees.csv')
    # Get dictionary with the department as the key and the number of employees in the department as the value.
    dictionary = process_data(employee_list)
    # Write the dictionary to a text file.
    filename = "report.txt"
    write_report(dictionary, filename)
    print("\n\"{}\" successfully created".format(filename))


if __name__ == '__main__':
    main()

