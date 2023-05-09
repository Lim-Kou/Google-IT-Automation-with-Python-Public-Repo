#!/usr/bin/env python3

import os
import subprocess
import requests
import time
import atexit


def start_server(ip_address):
    """Start the webserver, ask for user confirmation before closing the database
    connection, Only on local machine exclusively, and not on Google qwiklabs VM."""

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
        # Terminate the web server process when the script ends
        web_server_process.terminate()
        web_server_process.wait()

    if ip_address == "127.0.0.1:8000":
        web_server_process = subprocess.Popen(["fruitstore/manage.py", "runserver"], stdout=subprocess.DEVNULL,
                                              stderr=subprocess.DEVNULL)
        # Sleep for 1 sec while the server start up
        time.sleep(1)
        # Register the confirm_before_cleanup function to be executed at exit
        atexit.register(confirm_before_cleanup)


def main():
    """
    If on local machine: start the webserver, check if the images to be uploaded is on the local drive,
    if True, delete the old copy and upload the new one.
    If on Google qwiklabs VM: upload the images to the server.
    """
    # Directory path for images
    directory = "supplier-data/images"
    # For Google qwiklabs.com
    # url = "http://localhost/upload/"
    # ip_address = "http://localhost"
    # For local machine
    url = "http://127.0.0.1:8000/upload/"
    ip_address = "127.0.0.1:8000"

    # Start the Webserver if running in local machine
    start_server(ip_address)

    # For items in the images directory
    for infile in sorted(os.listdir(directory)):
        # If it is an image file
        if infile.endswith(".jpeg"):
            # Phrase path for item
            infile_loc = os.path.join(directory, infile)
            if ip_address == "127.0.0.1:8000":
                # Delete file if it exits
                outfile_loc = os.path.join("fruitstore/media/images", infile)
                if os.path.exists(outfile_loc):
                    os.remove(outfile_loc)

            with open(infile_loc, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
                if r.status_code == 201:
                    print("{} has been successfully uploaded.".format(infile))
                else:
                    print(
                        "\033[91m{} has not been successfully uploaded, with an error code of {} and text: \033[0m{}".format(
                            infile, r.status_code, r.request.body.decode("utf-8")))


if __name__ == '__main__':
    main()
