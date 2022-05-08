"""
Controller for our python code.

Gets input for the header, sender, and body from the user. Creates instance of
model.
"""
# import the regex package for searching for dates
import re
# import a function to convert strings to dates
from dateparser import parse
# import a function to add time
from datetime import timedelta
from datetime import date
import imaplib
from nntplib import decode_header
import email
import re

class Controller():
    """
    Controller for our python code.

    Gets input for the header, sender, and body from the user. Creates instance of
    model.
    """

    def __init__(self, username, password):
        [header, sender, body] = get_mail(username, password)
        self._recipient = sender
        self._header = header
        self._body = body

    # defines a property so header and sender can be accessed later
    @property
    def recipient(self):
        return self._recipient

    @property
    def header(self):
        return self._header

    # does this function also account for start and end times, or only dates? also, how do we incorporate the am/pm stuff? 
    def datetimes(self):
        """
        Returns the starting and ending date and time found in the text.

        Args:
            self: controller object (does not need to be explicitly called).

        Returns:
            Either a list of 2 elements containing the start and end date
            time date elements or the logical operator False if no time
            is found.
        """
        # calls get_date to find the date from the body text
        date = get_date(self._body)

        # if the body doesn't have a date in it, checks the header for a date
        if date==False:
            date = get_date(self._header)

        return date


# helper function for get_date
def set_am_pm(start_time, end_time):
    """
    Takes two strings representing hour increments and determines if they
    should be am or pm.

    Args:
        start_time: a string representing the start of a time range
        end_time: a string representing the end of a time range

    Returns:
        A list of two containing the start and end time strings but with the
        proper period marcation at the end of them.
    """

    # create an integer of the hour spot for comparison for both times
    start_int = int(re.findall(r"(?:\d{1,2})", start_time, re.IGNORECASE)[0])
    end_int = int(re.findall(r"(?:\d{1,2})", end_time, re.IGNORECASE)[0])

    # create logical checks if the time is am or pm
    is_am_start = "am" in str.lower(start_time)
    is_pm_start = "pm" in str.lower(start_time)
    is_am_pm_start = is_am_start is True or is_pm_start is True
    is_am_end = "am" in str.lower(end_time)
    is_pm_end = "pm" in str.lower(end_time)
    is_am_pm_end = is_am_end is True or is_pm_end is True

    # if either are missing an am or pm marker
    while is_am_pm_start is False or is_am_pm_end is False:
        # create logical checks if the time is am or pm in loop so they are updated
        is_am_start = "am" in str.lower(start_time)
        is_pm_start = "pm" in str.lower(start_time)
        is_am_pm_start = is_am_start is True or is_pm_start is True
        is_am_end = "am" in str.lower(end_time)
        is_pm_end = "pm" in str.lower(end_time)
        is_am_pm_end = is_am_end is True or is_pm_end is True

        # check if there is one in end time but not the other
        if is_am_pm_end is True and is_am_pm_start is False:
            if start_int == 12:
                if is_pm_end is True:
                    start_time += " pm"
                else:
                    start_time += " am"
            elif end_int == 12:
                if is_pm_end is True:
                    start_time += " am"
                else:
                    start_time += " pm"
            elif is_am_end is True:
                if start_int < end_int:
                    start_time += " am"
                else:
                    start_time += " pm"
            else:
                if start_int < end_int:
                    start_time += " pm"
                else:
                    start_time += " am"

        # check if there is one in the start time but not the end
        if is_am_pm_end is False and is_am_pm_start is True:
            if end_int == 12:
                if is_pm_start == True:
                    end_time += " am"
                else:
                    end_time += " pm"
            elif start_int == 12:
                if is_pm_start == True:
                    end_time += " pm"
                else:
                    end_time += " am"
            elif is_am_start is True:
                if start_int < end_int:
                    end_time += " am"
                else:
                    end_time += " pm"
            else:
                if start_int < end_int:
                    end_time += " pm"
                else:
                    end_time += " am"

        # check if neither start or end time have am or pm
        if is_am_pm_end is False and is_am_pm_start is False:
            if start_int == 12:
                start_time += " pm"
            elif end_int == 12:
                end_time += " pm"
            else:
                # if either are missing an am or pm marker
                end_time += " pm"

    return [start_time,end_time]

def get_date(text):
    """
    Takes a string and finds the start and end time of an event
    mentioned in the string. If there is a start time but no
    end time then an end time one hour later than the start time
    will be assumed.

    Args:
        text: a string that should be the header or body of an email

    Returns:
        Either a list of 2 elements containing the start and end date
        time date elements or the logical operator False if no time
        is found.
    """

    # variable to keep track of if a time exists
    time_exist = True

    # variable to keep track of if date exists
    date_exist = True

    # create the regex for finding time
    time_regex = r"(?:\d+:?\d*\s*(?:AM|PM)?\s*(?:-|–|to)\s*\d+:?\d*\s*(?:AM|PM)?)" +\
    r"|(?:\d+:?\d*\s*(?:AM|PM))|" +\
    r"(?<=at)\s*\d{1,2}:?\d*(?!.*(?:pm|am|-|–|to))"

    # attempt to find the times located in the body text
    try:
        time_extract = re.findall(time_regex, text, re.IGNORECASE)

        # if the time is blank then there is no time
        if time_extract[0] == "":
            time_exist = False
    except:
        # if the code ran into an error there is no time
        time_exist = False

    # create the regex for finding the date
    date_regex = r"(?:today)|(?:tomorrow)" +\
        r"|(?:(?:apr|may|jun|jul|aug|sep|oct|nov|dec|jan|feb|mar)\w*\s*\d+)" +\
        r"|(?:\d+/\d+/?\d*)"

    # attempt to find the dates located in the body text
    try:
        date_extract = re.findall(date_regex, text, re.IGNORECASE)
        # if the date is blank then there is no date
        if date_extract[0] == "":
            date_exist = False
            date_extract = " "
    except:
        # if the code ran into an error there is no date
        date_exist = False
        date_extract = " "

    # if a time has been found
    if time_exist is True:
        # using the date, we want to find the time by closest proximity
        if date_exist is True:
            date_index = text.index(date_extract[0])
            index_distances = []

            # ideally, we want to only use times with markers so we search for those
            marker_times = []
            for times in time_extract:
                if "am" in times.lower() or "pm" in times.lower():
                    marker_times.append(times)
            # if there are any marker times make it the time list
            if len(marker_times) > 0:
                time_extract = marker_times
            # find the index distance of each time in the list
            for times in time_extract:
                time_index = text.index(times)
                index_distances.append(abs(date_index - time_index))

            #choose the closest proximity time to date
            time_extract = time_extract[index_distances.index(min(index_distances))]

        else:
            # if there is no date just choose the first time
            time_extract = time_extract[0]

        # test if there is a seperator in the time
        sep_check = "-" in time_extract or "–" in time_extract or " to " in str.lower(time_extract)

        # find the current year so that the date is correct
        current_date = date.today()

        if sep_check is True:
            start_time_regex = r"(?:\d+:?\d*\s*(?:am|pm)?\s*)(?=-|–|to)"
            end_time_regex = r"(?:(?<=-)|(?<=–)|(?<=to))(?:\s*\d+:?\d*\s*(?:am|pm)?)"

            # take the time before the separator
            start_time = re.findall(start_time_regex, time_extract, re.IGNORECASE)
            start_time = start_time[0]

            # take the time after the seperator
            end_time = re.findall(end_time_regex, time_extract, re.IGNORECASE)
            end_time = end_time[0]

            # now make sure both times have an am or pm
            set_times = set_am_pm(start_time, end_time)

            start_time = set_times[0]

            end_time = set_times[1]

            # create the start and end date
            start_date = parse(date_extract[0] + " " + start_time, settings={'PREFER_DATES_FROM': 'future'})
            end_date = parse(date_extract[0] + " " + end_time, settings={'PREFER_DATES_FROM': 'future'})

            # make sure the year is current
            start_date = start_date.replace(year = current_date.year)

            end_date = end_date.replace(year = current_date.year)

            return [start_date,end_date]

        else:
            # if there is no end time create a 1 hour time slot
            start_time = time_extract

            if "am" not in str.lower(start_time) and "pm" not in str.lower(start_time):
                start_time += " pm"

            start_date = parse(date_extract[0] + " " + start_time, settings={'PREFER_DATES_FROM': 'future'})

            end_date = start_date + timedelta(hours=1)

            # make sure the year is current
            start_date = start_date.replace(year = current_date.year)
            end_date = end_date.replace(year = current_date.year)
            return [start_date,end_date]
    else:
        # return a boolean showing that there is no date/time
        return False

def get_mail(username, password):
    """
    Searches for a new email in the youcanical@gmail.com inbox and decodes
    the received email's subject, sender, and body.

    Args:
        username: a string representing an email username
        password: a string representing an email password
    Returns:
        A list containing three strings representing the subject,
        sender, and body. If there is no body, a list containing subject,
        sender, and None will be returned.
    """

    # define the encrypted connection path to gmail
    mail = imaplib.IMAP4_SSL("imap.gmail.com", port = 993)

    # login to the gmail account
    mail.login(username, password)


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

    # decode the email sender for reference
    reference_sender = decode_header(email_message.get("From"))
    # use regex to extract the email address
    reference_sender = re.findall(r"(?:(?<=<).*(?=>))", reference_sender, re.IGNORECASE)[0]
    sender = reference_sender

    # now continuously scrape the first email until it changes
    while subject == reference_subject and sender == reference_sender:
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
            mail.login(username, password)
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
