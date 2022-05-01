from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from create_ical import create_ical
import email
import datetime

def send_invite(receiver, ical_path):
    """
    Send an event as a calendar invitation. 

    Args: 
        receiver: a string with the recieving email address
        ical_path: a string representing the path to the ical file
    """

    sender = "youcanical@gmail.com"

    subject = 'iCal for __event__'
    body = 'Hi there, you requested an ical for __event__.'
    msg = MIMEMultipart('mixed')
    # time = datetime.now().strftime("%d/%m/%Y %H:%M")
    # msg['Date'] = time
    msg['Subject'] = subject
    msg['To'] = receiver

    part_email = MIMEText(body, 'html')

    with open(ical_path, 'r') as f:
        ical = f.read()
    part_cal = MIMEText(ical, 'calendar;method=REQUEST')

    msg.attach(part_email)
    msg.attach(part_cal)

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = 'uehiuheiufhureihweui34297238974898hdioj3hui4wehdogwalkedthedock' #input("Type your password and press enter: ")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        print("ical invite sent")
        server.sendmail(sender, receiver, msg)
        

send_invite('igoyal@olin.edu', 'test_icals/potato_test.ics')
