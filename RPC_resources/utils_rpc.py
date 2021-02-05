# !/usr/local/bin/python

# HTTP
import requests
# SCTP
# https://docs.python.org/3/library/email.examples.html
import smtplib
# https://pypi.org/project/beautifulsoup4/
from bs4 import BeautifulSoup
# for the header of the email message
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText

# from email.mime.multipart import MIMEMultipart
# from email.mime.multitext import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
# SMTP
# https://tools.ietf.org/html/rfc822.html

import csv
import numpy as np


# SMTP protocol
def send_message(Tag_Words_Input, input_message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # this password is generated with "google app passwords"
    from_mail = '@gmail.com'
    to_mail = '@gmail.com'
    password = ''
    server.login(from_mail, password)

    # message
    message = MIMEMultipart()
    message['From'] = from_mail
    message['To'] = to_mail
    message['Subject'] = 'Founded Tags: ' + str(input_message)
    body = 'Check the link: ' + str(input_message)
    # message = ("From: %s\r\nTo: %s\r\n\r\n"
    #       % (from_mail, to_mail))
    # message = message + subject + body
    message.attach(MIMEText(body, 'plain'))
    message = message.as_string()
    # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail
    server.sendmail(from_mail, to_mail, message)
    # debug final message
    # print(message)
    print('Send Success!')

    # finnaly end server session
    server.quit()


def urlListInput(file_input):
    urlList = []
    with open(file_input, 'rt') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in file_reader:
            urlList.append(row)

    return urlList

