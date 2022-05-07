from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.encoders
import smtplib, ssl
import email

def send_invite(ical_path, model, username, password):
    """
    Send an event as a calendar invitation.

    Args:
        ical_path: a string representing the path to the ical file
        model: a model class that stores all of the information needed to create an ical
        username: a string representing an email username
        password: a string representing an email password
    """
    # creates convenient variables
    receiver = model.recipient
    sender = username

    # some data cleaning to avoid having Fw: as part of the event's name
    name = model.name.replace('Fw: ', '')

    # define the subject and body of the email
    subject = f'iCal for {name}'
    body = f'Hi there, you requested an ical for {name}.'

    # create an object for the message
    msg = MIMEMultipart()

    # add the body and subject line text to the message
    msg.attach(MIMEText(body))
    msg['Subject'] = subject

    # add the ical attachment to the email
    attachment = MIMEBase('application', "octet-stream")
    with open(ical_path, "rb") as f:
        data = f.read()
    # the data we want as part of the attachment is the text from the ics file
    attachment.set_payload(data)
    # have to encode it to send as an attachment
    email.encoders.encode_base64(attachment)
    msg.attach(attachment)
    # adding the header tells it what type of file to expect. this sets the
    # header to the name of the ical file, including the .ics bit, which is
    # what makes it show up as something that can be added to one's calendar
    attachment.add_header('Content-Disposition', "attachment; filename= %s" % ical_path)

    # setup email server
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = password

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password) # login to the bot's email account
        # converts message back to string so that it's readable in the email
        text = msg.as_string()
        server.sendmail(sender, receiver, text) # sends the mail

    return
