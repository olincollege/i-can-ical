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
    import re

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
        # create logical checks if the time is am or pm
        is_am_start = "am" in str.lower(start_time)
        is_pm_start = "pm" in str.lower(start_time)
        is_am_pm_start = is_am_start is True or is_pm_start is True
        is_am_end = "am" in str.lower(end_time)
        is_pm_end = "pm" in str.lower(end_time)
        is_am_pm_end = is_am_end is True or is_pm_end is True
        # check if there is one in end time but not the other
        if is_am_pm_end is True and is_am_pm_start is False:
            if is_am_end is True:
                if start_int < end_int:
                    start_time += " am"
                else:
                    start_time += " pm"
            else:
                if start_int < end_int:
                    start_time += " pm"
                else:
                    start_time += " am"
        # check if there is one in the start time but not other
        if is_am_pm_end is False and is_am_pm_start is True:
            if is_am_start is True:
                if start_int < end_int:
                    end_time += " am"
                else:
                    end_time += " pm"

        # check if neither start or end time have am or pm
        if is_am_pm_end is False and is_am_pm_start is False:
            end_time += " pm"            # if either are missing an am or pm marker
    while is_am_pm_start is False or is_am_pm_end is False:
        # create logical checks if the time is am or pm
        is_am_start = "am" in str.lower(start_time)
        is_pm_start = "pm" in str.lower(start_time)
        is_am_pm_start = is_am_start is True or is_pm_start is True
        is_am_end = "am" in str.lower(end_time)
        is_pm_end = "pm" in str.lower(end_time)
        is_am_pm_end = is_am_end is True or is_pm_end is True
        # check if there is one in end time but not the other
        if is_am_pm_end is True and is_am_pm_start is False:
            if is_am_end is True:
                if start_int < end_int:
                    start_time += " am"
                else:
                    start_time += " pm"
            else:
                if start_int < end_int:
                    start_time += " pm"
                else:
                    start_time += " am"
        # check if there is one in the start time but not other
        if is_am_pm_end is False and is_am_pm_start is True:
            if is_am_start is True:
                if start_int < end_int:
                    end_time += " am"
                else:
                    end_time += " pm"

        # check if neither start or end time have am or pm
        if is_am_pm_end is False and is_am_pm_start is False:
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

            if "am" not in str.lower(start_time) or "pm" not in str.lower(start_time):
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

test = get_date("Babyshower Power Hour 8:55-9:55 pm 2NN EOM")

print(test)