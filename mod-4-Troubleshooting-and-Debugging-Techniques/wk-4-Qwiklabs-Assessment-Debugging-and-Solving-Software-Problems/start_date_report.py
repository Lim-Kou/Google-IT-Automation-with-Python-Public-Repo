#!/usr/bin/env python3


import csv
import datetime
import requests
import bisect
import concurrent.futures

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    # Download the file over the internet.
    response = requests.get(url, stream=True)
    # Create an empty list.
    lines = []
    # Append lines to the empty list.
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines


def get_start_date():
    """Interactively get the start date to query for."""
    print('\nGetting the first start date to query for.\n')
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)


def list_newer(start_date, data):
    """ Prints out the start date and name of any personals that starts working after the user specified start date."""
    def get_same_or_newer(start_date):
        """Returns the employees that started on the given date, or the closest one."""
        reader = csv.reader(data[1:])
        rows = list(reader)
        # Sort the rows based on a specific column (e.g., column index 0)
        sorted_rows = sorted(rows, key=lambda x: x[3])
        # get all the dates that from sorted rows
        date_strings = [row[3] for row in sorted_rows]
        # convert date object to string
        date_string = start_date.strftime("%Y-%m-%d")
        # Find the index where the date is larger than start date
        index = bisect.bisect_right(date_strings, date_string)
        return index, sorted_rows

    # Retrieve the index and sorted rows corresponding to dates that are equal to or later than the start date.
    index, sorted_rows = get_same_or_newer(start_date)
    for row in sorted_rows[index:]:
        formatted_date = datetime.datetime.strptime(row[3], "%Y-%m-%d").strftime("%b %d, %Y")
        print("Started on {}: {}".format(formatted_date, [row[0] + " " + row[1]]))


def threads():
    """Concurrently run and return the output of the two functions: get_file_lines and get_start_date."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        get_data = executor.submit(get_file_lines, FILE_URL)
        get_date = executor.submit(get_start_date)

    data = get_data.result()
    start_date = get_date.result()

    return data, start_date


def main():
    """Concurrently get user input for start date and download the data from the specified url. Process the data and
    prints out the start date and name of any personals that starts working after the specified start date."""
    # Download the data first wile getting user input for start date.
    data, start_date = threads()
    # print out the personals that started later than user inputted start date.
    list_newer(start_date, data)


if __name__ == "__main__":
    main()
