#!/usr/bin/env python

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.utils import formatdate
import smtplib
from sys import argv

from account import username, password

fromaddr = argv[1]
toaddr = argv[1]
message = MIMEMultipart()
message['From'] = fromaddr
message['To'] = toaddr
message['Date'] = formatdate(localtime=True)
message['Subject'] = argv[2]

body = argv[3]

message.attach(MIMEText(body, 'plain'))
text = message.as_string()

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddr,toaddr,text)
server.close()

