#!/usr/bin/env python3
import sys
import re


def error_search(log_file):
    """Get error from user and search the log file for any lines that contains the specified error."""
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    print(returned_errors)
    return returned_errors


def file_output(returned_errors):
    """write the errors in to log file named 'errors_found.log'."""
    with open('errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


def main():
    """Get the log file location from argv[1], ask user for the error code, search for the error in the log file and
    write the searched results into a log file named 'errors_found.log'."""
    # Get the log file location from argv[1]
    log_file = sys.argv[1]
    # Ask user for the error code and search for the error in the log file
    returned_errors = error_search(log_file)
    # Write the searched results into a log file named 'errors_found.log'.
    file_output(returned_errors)
    print("\"errors_found.log\" successfully created")
    sys.exit(0)


if __name__ == '__main__':
    main()

# Make file executable
# sudo chmod +x find_error.py

# Usage for main:
# ./find_error.py fishy.log

# Error
# CRON ERROR Failed to start
