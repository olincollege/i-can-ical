"""
The view for i-can-ical.
"""
from datetime import datetime
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.encoders
import smtplib
import ssl
import icalendar as ical

class View():
    """
    The view for ican-ical draws from the model to create and send an ics file
    to the user.

    It relies on helper functions create_ical() and send_invite().

    Attributes:
        _model: an icanical Model object that represents the event
        _username: a string with the email address being used to send the ical
        _password: a string with the password for the address above
    """

    def __init__(self, model, username, password):
        self._model = model
        self._username = username
        self._password = password

        # all icals will be created at this filepath so that it's not storing
        # icals for old events
        self._filepath = 'test_icals/actual_ical.ics'

    def send_ical(self):
        """
        Creates an ical based on the information in the model object. Then
        sends the ical.
        """
        create_ical(self._filepath, self._model)
        send_invite(self._filepath, self._model, self._username, self._password)
        print('ical invite sent')


def create_ical(filepath, model):
    """
    Take parsed data and turn it into an ical. The ical file will be saved [here].

    Args:
        filepath: a string specifying the path to where the ics file should be
            generated.
        model: an ical model object which represents an event. It holds all of
            the necessary information to make an ical.
    """
    # pulls information from the model and sets them to convenient variables
    name = model.name
    start_datetime = model.start
    end_datetime = model.end
    recipient = model.recipient

    # creates a calendar object that the event can then be added to
    cal = ical.Calendar()
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('version', '3.0')
    cal.add('attendee', 'MAILTO:igoyal@olin.edu')

    # creates an event object
    event = ical.Event()
    event.add('summary', name)

    # converts date and time to standard format. sets timezone as eastern.
    event.add('dtstart', start_datetime)
    event.add('dtend', end_datetime)
    # the time the calendar event was created
    event.add('dtstamp', datetime.today())

    # sets recipient/attendee
    attendee = ical.vCalAddress(recipient)
    attendee.params['ROLE'] = ical.vText('REQ-PARTICIPANT')
    event.add('attendee', recipient, encode=0)

    # adds event to calendar
    cal.add_component(event)

    # opens file, converts information to ical format, and closes file
    with open(filepath, 'wb') as file:
        file.write(cal.to_ical())

    # now the ics file has been created at the specified filepath
    # the function doesn't return anything

def send_invite(ical_path, model, sender, password):
    """
    Send an event as a calendar invitation.

    Args:
        ical_path: a string representing the path to the ical file
        model: a model class that stores all of the information needed to
            create an ical
        sender: a string representing an email username
        password: a string representing an email password
    """
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
    attachment.add_header('Content-Disposition', "attachment; filename= %s" % \
         ical_path)

    # setup email server
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password) # login to the bot's email account
        # converts message back to string so that it's readable in the email
        text = msg.as_string()
        server.sendmail(sender, model.recipient, text) # sends the mail
