import os
import pandas as pd
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


with open('email_list1.csv', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for i, row in enumerate(csv_reader):
        msg = MIMEMultipart()
        msg['To'] = row[1]
        msg['Subject'] = 'Certificate of Completion'

        # Add a message body
        body = 'Congratulations on completing the course!'
        msg.attach(MIMEText(body, 'plain'))

        # Attach the certificate to the message
        certificate_path = row[2]
        certificate = open(certificate_path, 'rb')
        certificate_part = MIMEApplication(certificate.read(), _subtype='pdf')
        certificate_part.add_header('Content-Disposition', 'attachment', filename='certificate.pdf')
        msg.attach(certificate_part)

        # Send the message using SMTP
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'genyk.b@gmail.com'
        smtp_password = 'hahjcnfaxjzljshh'
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, row[1], msg.as_string())
        server.quit()
