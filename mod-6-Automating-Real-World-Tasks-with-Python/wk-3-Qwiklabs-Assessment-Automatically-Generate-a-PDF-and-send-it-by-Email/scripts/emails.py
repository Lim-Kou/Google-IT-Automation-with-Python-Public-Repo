#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

# Make sure all required keys are set:
if not os.environ.get("OUTLOOK_email") or not os.environ.get("GOOGLE_email") or not os.environ.get("GOOGLE_passkey"):
    raise RuntimeError(
        "Run in terminal instead of Pycharm Run and/or set OUTLOOK_email, GOOGLE_email and GOOGLE_passkey in ~/.profile")


def generate(sender, recipient, subject, body, attachment_path=None):
    """Creates an email with an optional attachment."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path is not None:
        # Process the attachment and add it to the email
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)

    return message


def send(message):
    """Sends the message to the configured SMTP server."""
    # For Lab
    # server = 'localhost'
    # For local machine
    server = 'smtp.gmail.com'
    if server == 'smtp.gmail.com':
        mail_server = smtplib.SMTP_SSL(server)
        mail_server.set_debuglevel(1)
        print("\nUsing gmail to login...\n")
        sender = os.environ.get("GOOGLE_email")
        mail_pass = os.environ.get("GOOGLE_passkey")
        mail_server.login(sender, mail_pass)
    else:
        mail_server = smtplib.SMTP(server)

    # mail_server.set_debuglevel(1)
    mail_server.send_message(message)
    mail_server.quit()
