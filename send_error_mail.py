from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

def send_error_mail(receiver, username, password):
    """
    Send an email informing the user that an ical couldn't be created.

    Args:
        receiver: string representing the receiver of the error email.
        username: string representing the email address of the bot
        password: string representing the password of the bot
    """
    sender = username

    subject = f'iCal could not be created' # add in a line to actually use the subject
    body = f'Hi, we could not create an ical for your event. Please make sure\
    your email contains either a date or time.'

    msg = MIMEMultipart()

    msg.attach(MIMEText(body))

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = password

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        text = msg.as_string()
        server.sendmail(sender, receiver, text)

    return
