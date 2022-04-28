"""
Controller for our python code.

Gets input for the header, sender, and body from the user. Creates instance of
model.
"""

sender = input('Input sender\'s name or email address')
header = input('Input header of event (or subject line of email).')
body = input('Input body text of email. Make sure it includes a date/time.')

class controller():
    """
    Controller for our python code.

    Gets input for the header, sender, and body from the user. Creates instance of
    model.
    """


    def __init__(self):
        pass

    def get_date(self, body, header):
        # import the regex package for searching for dates
        import re
        # import a package to convert strings to dates
        from dateparser import parse

        # variable to keep track of if a time exists
        time_exist = True

        # variable to keep track of if date exists
        date_exist = True

        # create the regex for finding time
        time_regex = r"(?:\d+:?\d*\s*(?:AM|PM)" +\
        r"?\s*(?:-|–|to)\s*\d+:?\d*\s*(?:AM|PM)?)" +\
        r"|(?:\d+:?\d*(?:AM|PM))"

        # attempt to find the times located in the body text
        try:
            time_extract = re.findall(time_regex, body, re.IGNORECASE)
            # if the time is blank then there is no time
            if time_extract[0][0] == "":
                time_exist = False
        except:
            # if the code ran into an error there is no time
            time_exist = False

        # create the regex for finding the date
        date_regex = r"(?:today)|(?:tomorrow)" +\
            r"|(?:\w*\s?\d+\s?(?:th|nd|rd|st))|(?:\d+/\d+/?\d*)"

        # attempt to find the dates located in the body text
        try:
            date_extract = re.findall(date_regex, body, re.IGNORECASE)
            # if the date is blank then there is no date
            if date_extract[0][0] == "":
                date_exist = False
        except:
            # if the code ran into an error there is no date
            date_exist = False

        # if the body doesn't have a time then we need to check the header
        if time_exist is False:
            time_exist = True
            date_exist = True

            # attempt to find the date and time in the header
            try:
                time_extract = re.findall(time_regex, header, re.IGNORECASE)
                # if the time is blank then there is no time
                if time_extract[0][0] == "":
                    time_exist = False
            except:
                # if the code ran into an error there is no time
                time_exist = False

            # attempt to find the dates located in the body text
            try:
                date_extract = re.findall(date_regex, header, re.IGNORECASE)
                # if the date is blank then there is no date
                if date_extract[0][0] == "":
                    date_exist = False
            except:
                # if the code ran into an error there is no date
                date_exist = False




