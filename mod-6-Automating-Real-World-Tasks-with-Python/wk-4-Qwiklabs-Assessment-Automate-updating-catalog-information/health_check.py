#!/usr/bin/env python3

import psutil
import socket
import time
import emails
import os

# For lab
# sender = "automation@example.com"
# username = "student-03-dbb2c0876961"
# receiver = "{}@example.com".format(username)

# For local machine
sender = os.environ.get("GOOGLE_email")
receiver = os.environ.get("GOOGLE_email")


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        email = emails.generate_email(sender=sender, recipient=receiver, subject="Error - CPU usage is over 80%",
                                      body="Please check your system and resolve the issue as soon as possible.")
        emails.send_email(email)


def check_disk_space():
    disk_usage = psutil.disk_usage("/")
    disk_free_percentage = disk_usage.free / disk_usage.total * 100
    if disk_free_percentage < 20:
        email = emails.generate_email(sender=sender, recipient=receiver,
                                      subject="Error - Available disk space is less than 20%",
                                      body="Please check your system and resolve the issue as soon as possible.")
        emails.send_email(email)


def check_memory():
    memory_usage = psutil.virtual_memory()
    if memory_usage.available < 500 * 1024 * 1024:  # 500MB in bytes
        email = emails.generate_email(sender=sender, recipient=receiver,
                                      subject="Error - Available memory is less than 500MB",
                                      body="Please check your system and resolve the issue as soon as possible.")
        emails.send_email(email)


def check_hostname_resolution():
    try:
        ip_address = socket.gethostbyname("localhost")
        if ip_address != "127.0.0.1":
            email = emails.generate_email(sender=sender, recipient=receiver,
                                          subject="Error - localhost cannot be resolved to 127.0.0.1",
                                          body="Please check your system and resolve the issue as soon as possible.")
            emails.send_email(email)
    except socket.error:
        print("\033[91mError: Hostname 'localhost' cannot be resolved\033[0m")


def check_system_statistics():
    while True:
        check_cpu_usage()
        check_disk_space()
        check_memory()
        check_hostname_resolution()
        time.sleep(60)  # Wait for 60 seconds


def main():
    check_system_statistics()


if __name__ == '__main__':
    main()
