import imaplib
from nntplib import decode_header
import email
import re

def get_mail():
    """
    Searches for a new email in the youcanical@gmail.com inbox and decodes
    the received email's subject, sender, and body.

    Returns:
        A list containing three strings representing the subject,
        sender, and body. If there is no body, a list containing subject,
        sender, and None will be returned.
    """
    # define the email of the bot
    _email_user = "youcanical@gmail.com"
    # define the password of the bot
    _email_pass = "uehiuheiufhureihweui34297238974898hdioj3hui4wehdogwalkedthedock"

    # define the encrypted connection path to gmail
    mail = imaplib.IMAP4_SSL("imap.gmail.com", port = 993)

    # login to the gmail account
    mail.login(_email_user, _email_pass)


    # select the folder we want to read mail from
    mail.select('Inbox')

    # searches for mail with no filter, typ tells if the request was valid and data is the id's of the emails
    (typ, data) = mail.search(None, "ALL")

    # select the id's of the emails from the list and separate the id's into separate list elements
    mail_ids = data[0]
    mail_ids = mail_ids.split()

    # fetch the first email, RFC822 is the internet protocol
    (typ, data) = mail.fetch(mail_ids[-1], '(RFC822)')
    # data is a list containing a tuple then bytes the main parts of the email
    # are located in the second item in the tuple


    # parse the email in bytes into a message object
    email_message = email.message_from_bytes(data[0][1])

    # decode the email subject that the code will compare to detect a new email
    reference_subject = decode_header(email_message["Subject"])
    subject = reference_subject

    # now continuously scrape the first email until it changes
    while subject == reference_subject:
        # try to scrape the emails or login again if unsuccessful
        try:
            # select the folder we want to read mail from
            mail.select('Inbox')

            # searches for mail with no filter, typ tells if the request was valid and data is the id's of the emails
            (typ, data) = mail.search(None, "ALL")

            # select the id's of the emails from the list and separate the id's into separate list elements
            mail_ids = data[0]
            mail_ids = mail_ids.split()

            # fetch the first email, RFC822 is the internet protocol
            (typ, data) = mail.fetch(mail_ids[-1], '(RFC822)')
            # data is a list containing a tuple then bytes the main parts of the email
            # are located in the second item in the tuple


            # parse the email in bytes into a message object
            email_message = email.message_from_bytes(data[0][1])
        except:
            # the bot may have been logged out so if scraping fails retry the login

            # define the encrypted connection path to gmail
            mail = imaplib.IMAP4_SSL("imap.gmail.com", port = 993)

            # login to the gmail account
            mail.login(_email_user, _email_pass)
            # select the folder we want to read mail from
            mail.select('Inbox')

            # searches for mail with no filter, typ tells if the request was valid and data is the id's of the emails
            (typ, data) = mail.search(None, "ALL")

            # select the id's of the emails from the list and separate the id's into separate list elements
            mail_ids = data[0]
            mail_ids = mail_ids.split()

            # fetch the first email, RFC822 is the internet protocol
            (typ, data) = mail.fetch(mail_ids[-1], '(RFC822)')
            # data is a list containing a tuple then bytes the main parts of the email
            # are located in the second item in the tuple


            # parse the email in bytes into a message object
            email_message = email.message_from_bytes(data[0][1])

        # decode the email subject
        subject = decode_header(email_message["Subject"])

        # decode the email sender
        sender = decode_header(email_message.get("From"))
        # use regex to extract the email address
        sender = re.findall(r"(?:(?<=<).*(?=>))", sender, re.IGNORECASE)[0]

        # walk iterates through the parts of the emails
        for part in email_message.walk():
            # only capture the parts of the email that are plain text
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                body = str(email.message_from_bytes(body))
    # Since forwarded emails have an extra date, we need regex to remove them
    body = re.sub(r"From:[\s\S]*Subject:", "", body, re.IGNORECASE)
    try:
        # if the email has a body this should work fine
        return[subject, sender, body]
    except:
        # if body does not exist return None in its place
        return[subject, sender, None]

test = get_mail()
print(test)