#! /usr/bin/env python3
# This is a practice file that contains codes from Coursera.


from email.message import EmailMessage
import os

# Make sure all required keys are set:
if not os.environ.get("OUTLOOK_email") or not os.environ.get("GOOGLE_email") or not os.environ.get("GOOGLE_passkey"):
    raise RuntimeError(
        "Run in terminal instead of Pycharm Run and/or set OUTLOOK_email, GOOGLE_email and GOOGLE_passkey in ~/.profile")


message = EmailMessage()
print(message)

sender = os.environ.get("GOOGLE_email")
recipient = os.environ.get("OUTLOOK_email")
subject = 'Greetings from {} to {}!'.format(sender, recipient)
body = """Hey there!

    I'm learning to send emails using Python!"""

# From, To, and Subject are examples of email header fields. They’re key-value pairs of labels and instructions
message['From'] = sender
message['To'] = recipient
message['Subject'] = subject

# Message body set_content() method also automatically added a couple of headers that the email infrastructure will
# use when sending this message to another machine.
message.set_content(body)

print(message)


# Attachments you  need to label the attachment with a MIME type and subtype to tell them what sort of file you’re
# sending. The Internet Assigned Numbers Authority (IANA) ( iana.org ) hosts a registry of valid MIME types . If you
# know the correct type and subtype of the files you’ll be sending, you can use those values directly. If you don't
# know, you can use the Python mimetypes module to make a good guess!
import os.path
import mimetypes
attachment_path = "example.jpg"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
#  The EmailMessage type needs a MIME type and subtypes as separate strings
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

print(message)


# Sending the Email Through an SMTP Server
# Use the Simple Mail Transfer Protocol (SMTP)
import smtplib
import getpass
import os

# Try to see if there is any local SMTP server configured
try:
    mail_server = smtplib.SMTP('localhost')
except ConnectionRefusedError:
    print("no local SMTP server configured")

# connect to the SMTP server for your personal email address
# 1. connect to a remote SMTP server using Transport Layer Security (TLS), making it HTTPS
# Using gmail
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)
print("\nUsing gmail to login...\n")


sender = os.environ.get("GOOGLE_email")
mail_pass = os.environ.get("GOOGLE_passkey")
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()

# If not using gmail:
# mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
# mail_server.set_debuglevel(1)
# sender = "me@example.com"
# mail_pass = getpass.getpass('Password? ')
# mail_server.login(sender, mail_pass)
# mail_server.quit()
