#! /usr/bin/env python3

import os
import subprocess
import requests
import time
import atexit


# Start the webserver first:
# corpweb/manage.py runserver
# Desired JSON Format: title, name, date and feedback
# {"name": "Test Fruit", "weight": 100, "description": "This is the description of my test fruit", "image_name": "icon.sheet.png"}

def extract_lines(path, filename):
    """Given a file path, open and return the lines as a list if the file is a text file."""
    # Phrase path for item
    infile = os.path.join(path, filename)
    # If it ends with .txt
    if filename.endswith("txt"):
        # Open the text file
        with open(infile, 'r') as file:
            lines = file.read().splitlines()
            lines = [line for line in lines if line.strip()]
        return lines


def retrieve_lines(filename, lines, expected_variables):
    """Given a list, ensure that the number of elements in the list matches the expected_variables parameter."""
    if len(lines) == expected_variables:
        return lines
    else:
        # Do not unpack the list and go the next txt file
        print("\033[91m{} does not have all required values, please check: {}.\033[0m".format(filename, lines))
        return None


def start_server(ip_address):
    """Start the webserver, reinitialize the database, ask for user confirmation before closing the database
    connection, Only on local machine exclusively, and not on Google qwiklabs VM."""
    def reinitialize_db():
        """Reinitialize the database, to avoid scrolling through multiple duplicate entries on the webserver."""
        command = 'fruitstore/manage.py flush'

        # Run the command and provide 'yes' as the input
        process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(input='yes\n')

        # Check the process return code
        if process.returncode == 0:
            print('\ndb.sqlite3 successfully reinitialized.\n')
        else:
            print(f'An error occurred: {error}')

    def confirm_before_cleanup():
        """Get user confirmation before closing the webserver connection."""
        while True:
            user_input = input("\nDo you want to exit the Webserver: http://127.0.0.1:8000 (yes/no): ")
            if user_input.lower() == "yes":
                # Perform cleanup tasks
                cleanup()
                break
            elif user_input.lower() == "no":
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def cleanup():
        """Terminate the web server process when the script ends"""
        web_server_process.terminate()
        web_server_process.wait()

    if ip_address == "127.0.0.1:8000":
        web_server_process = subprocess.Popen(["fruitstore/manage.py", "runserver"], stdout=subprocess.DEVNULL,
                                              stderr=subprocess.DEVNULL)
        # Sleep for 1 sec while the server start up
        time.sleep(1)
        # Clear all entries from db.sqlite3
        reinitialize_db()
        # Register the confirm_before_cleanup function to be executed at exit
        atexit.register(confirm_before_cleanup)


def post_request(ip_address, upload_directory, filename, feedback_dict):
    """Submit the data to the webserver."""
    response = requests.post("http://{}{}".format(ip_address,upload_directory), json=feedback_dict)
    if response.status_code == 201:
        print("{} has been successfully uploaded.".format(filename))
    else:
        print("\033[91m{} has not been successfully uploaded, with an error code of {} and text: \033[0m{}".format(
            filename, response.status_code, response.request.body.decode("utf-8")))


def main():
    """
    If using local machine: Start the webserver, reinitialize the database, upload the data, ask for user confirmation
    before closing the database connection.
    If using Qwiklabs: upload the data directly to the running webserver.
    """
    # For Lab
    # directory = "supplier-data/descriptions/"
    # ip_address of the webserver
    # ip_address = "34.66.222.66"
    # upload_directory = "/fruits/"

    # For local machine
    directory = "supplier-data/descriptions/"
    # ip_address of the webserver
    ip_address = "127.0.0.1:8000"
    upload_directory = "/fruits/"

    # Start the Webserver if running in local machine
    start_server(ip_address)

    # For each file in directory
    for filename in sorted(os.listdir(directory)):
        # Read all lines if file is a text file
        lines = extract_lines(directory, filename)
        # Retrieve required fields from lines, continue to the next txt file if fields are empty or partially empty.
        fields = retrieve_lines(filename, lines, 3)
        if fields is not None:
            name, weight, description = fields
        else:
            continue
        # Create dictionary in the desired format
        feedback_dict = {"name": name, "weight": int(weight.split()[0]), "description": description, "image_name": filename.split(".")[0]+".jpeg"}

        # post the dictionaries to the company's website
        post_request(ip_address, upload_directory, filename, feedback_dict)


if __name__ == '__main__':
    main()
