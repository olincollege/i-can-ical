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

    def get_date(self, text):
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
        # import the regex package for searching for dates
        import re
        # import a function to convert strings to dates
        from dateparser import parse
        # import a function to add time
        from datetime import timedelta

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
            time_extract = re.findall(time_regex, text, re.IGNORECASE)
            date_extract = date_extract[0]
            # if the time is blank then there is no time
            if time_extract[0] == "":
                time_exist = False
        except:
            # if the code ran into an error there is no time
            time_exist = False

        # create the regex for finding the date
        date_regex = r"(?:today)|(?:tomorrow)" +\
            r"|(?:\w*\s?\d+\s?(?:th|nd|rd|st))|(?:\d+/\d+/?\d*)"

        # attempt to find the dates located in the body text
        try:
            date_extract = re.findall(date_regex, text, re.IGNORECASE)
            date_extract = date_extract[0]
            # if the date is blank then there is no date
            if date_extract[0] == "":
                date_exist = False
        except:
            # if the code ran into an error there is no date
            date_exist = False
            date_extract = ""

        # if a time has been found
        if time_exist is True:
            # using the date, we want to find the time by closest proximity
            if date_exist is True:
                date_index = text.index(date_extract[0])
                index_distances = []
                # find the index distance of each time in the list
                for times in enumerate(time_extract):
                    time_index = text.index(times)
                    index_distances.append(abs(date_index - time_index))
                #choose the closest proximity time to date
                time_extract = time_extract[index_distances.index(min(index_distances))]
            else:
                # if there is no date just choose the first time
                time_extract = time_extract[0]

            # test if there is a seperator in the time
            sep_regex = r"(?:\d+:?\d*\s*(?:AM|PM)?\s*(?:-|–|to)" + \
            r"\s*\d+:?\d*\s*(?:AM|PM)?)"
            sep_check = re.match(sep_regex, time_extract, re.IGNORECASE)

            if sep_check is True:
                start_time_regex = r"(?:\d+:?\d*\s*(?:am|pm)?\s*)(?=-|–|to)"
                end_time_regex = r"(?<=-|–|to)(?:\s*\d+:?\d*\s*(?:am|pm)?)"

                # take the time before the seperator
                start_time = re.findall(start_time_regex, time_extract, re.IGNORECASE)
                start_time = start_time[0]
                # take the time after the seperator
                end_time = re.findall(end_time_regex, time_extract, re.IGNORECASE)
                end_time = end_time[0]

                # create the start and end date
                start_date = parse(date_extract[0] + " " + start_time)
                end_date = parse(date_extract[0] + " " + end_time)

                return [start_date,end_date]

            else:
                # if there is no end time create a 1 hour time slot
                start_date = parse(date_extract[0] + " " + start_time)
                end_date = start_date + timedelta(hours=1)

                return [start_date,end_date]
        else:
            # return a boolean showing that there is no date/time
            return False
