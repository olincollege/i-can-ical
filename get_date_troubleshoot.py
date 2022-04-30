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
    # import the regex package for searching for dates
    import re
    # import a function to convert strings to dates
    from dateparser import parse
    # import a function to add time
    from datetime import timedelta

    from datetime import date

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
        print(time_extract)
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
        print(date_extract)
        # if the date is blank then there is no date
        if date_extract[0] == "":
            date_exist = False
    except:
        # if the code ran into an error there is no date
        date_exist = False
        date_extract = ""
    print("time exist", time_exist)
    # if a time has been found
    if time_exist is True:
        # using the date, we want to find the time by closest proximity
        print("date_exist", date_exist)
        if date_exist is True:
            date_index = text.index(date_extract[0])
            print("date index", date_index)
            index_distances = []
            # find the index distance of each time in the list
            for times in time_extract:
                time_index = text.index(times)
                print("time index", time_index)
                index_distances.append(abs(date_index - time_index))
            print("index distances", index_distances)
            #choose the closest proximity time to date
            time_extract = time_extract[index_distances.index(min(index_distances))]
            print("minimum time distance", time_extract)
        else:
            # if there is no date just choose the first time
            time_extract = time_extract[0]

        # test if there is a seperator in the time
        sep_regex = r"(?:\d+:?\d*\s*(?:AM|PM)?\s*(?:-|–|to)" + \
        r"\s*\d+:?\d*\s*(?:AM|PM)?)"
        sep_check = re.search(sep_regex, time_extract, re.IGNORECASE)
        print("seperator check", sep_check)

        # find the current year so that the date is correct
        current_date = date.today()

        if sep_check is not None:
            start_time_regex = r"(?:\d+:?\d*\s*(?:am|pm)?\s*)(?=-|–|to)"
            end_time_regex = r"(?<=-|–|to)(?:\s*\d+:?\d*\s*(?:am|pm)?)"

            # take the time before the seperator
            start_time = re.findall(start_time_regex, time_extract, re.IGNORECASE)
            start_time = start_time[0]
            # take the time after the seperator
            end_time = re.findall(end_time_regex, time_extract, re.IGNORECASE)
            end_time = end_time[0]

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
            start_date = parse(date_extract[0] + " " + start_time, settings={'PREFER_DATES_FROM': 'future'})

            end_date = start_date + timedelta(hours=1)

            # make sure the year is current
            start_date = start_date.replace(year = current_date.year)

            end_date = end_date.replace(year = current_date.year)

            return [start_date,end_date]
    else:
        # return a boolean showing that there is no date/time
        return False

test = get_date("Boba party april 2nd 2022 at 4pm")

print(test)