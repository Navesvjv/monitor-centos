import os
import smtplib

from decouple import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class SendEmail:
    def __init__(self):
        self.emailFrom = 
