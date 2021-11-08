#!/usr/bin/python

"""
This script will do 2 parts:
(1) Fetch the target patient result file to a tmp directory that gets cleaned up after the script is run.
(2) Sends a secure email with result file as an attachment to non-BCM email addresses.
Currently, the script requires passing in:
(i) name of the patient result file
(ii) email address of the patient
OTHER REQUIREMENTS: Need to be in environment with aws configured.
EXAMPLE COMMAND LINE: python3 get_send_pdf_local.py 1_46548475643.pdf mahiraj@tamu.edu
NEXT STEPS: Stream s3 file to email without any download.
"""

import boto3
import botocore
import smtplib

from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
import sys
import tempfile


TMP_DIR = tempfile.TemporaryDirectory()


def run():
    get_pdf_from_s3(sys.argv[1])
    # sys.argv[1] is a string with name of s3 obj (ex: '1_46548475643.pdf')
    send_secure_email(sys.argv[2], sys.argv[1])
    # sys.argv[2] is a string with the email address of the recipient


def get_pdf_from_s3(obj_key):
    BUCKET_NAME = "covid19dev"  # replace with prod bucket name
    KEY = obj_key
    FILE_NAME = obj_key
    TMP_FILE = os.path.join(TMP_DIR.name, FILE_NAME)
    s3 = boto3.resource("s3")
    try:
        s3.Bucket(BUCKET_NAME).download_file(
            KEY, TMP_FILE
        )  # downloads the file into a tmp dir
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "404":
            print("The object does not exist.")
        else:
            raise


def send_secure_email(rec_email, obj_key):
    subject = "[SECURE] Results of COVID-19 Screening - Just a Test Attachment"
    body = "Results for your COVID-19 Screening is attached to this email."
    sender_email = "mahiraj@tamu.edu"
    receiver_email = rec_email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    files = [obj_key]
    for cov_file in files:
        tmp_file = os.path.join(TMP_DIR.name, cov_file)
        attachment = open(tmp_file, "rb")
        file_basename = os.path.basename(tmp_file)
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        part.add_header("Content-Disposition", "attachment", filename=file_basename)
        encoders.encode_base64(part)
        message.attach(part)
    text = message.as_string()
    s = smtplib.SMTP("smtp.bcm.edu")
    s.send_message(message)
    s.quit()


if __name__ == "__main__":
    run()
