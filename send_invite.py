from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.encoders
import smtplib, ssl
import email

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

    msg = MIMEMultipart()

    msg.attach(MIMEText(body))

    attachment = MIMEBase('application', "octet-stream")
    with open(ical_path, "rb") as f:
        data = f.read()
    attachment.set_payload(data)
    email.encoders.encode_base64(attachment)
    msg.attach(attachment)
    attachment.add_header('Content-Disposition', "attachment; filename= %s" % ical_path)

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = 'uehiuheiufhureihweui34297238974898hdioj3hui4wehdogwalkedthedock' #input("Type your password and press enter: ")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        print("logged in")
        text = msg.as_string()
        server.sendmail(sender, receiver, text)
        print("ical invite sent")

    return
        

send_invite('igoyal@olin.edu', 'test_icals/wood_swallow.ics')
