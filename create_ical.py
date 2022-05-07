"""
Use iCalendar package to create .ics file.
"""

import icalendar as ical
from datetime import datetime

def create_ical(filepath, model):
    """
    Take parsed data and turn it into an ical. The ical file will be saved [here].

    Args: 
        filepath: a string specifying the path to where the ics file should be generated.
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
    event.add('dtstamp', datetime.today()) # the time the calendar event was created

    # sets recipient/attendee
    attendee = ical.vCalAddress(recipient)
    attendee.params['ROLE'] = ical.vText('REQ-PARTICIPANT')
    event.add('attendee', recipient, encode=0)

    # adds event to calendar
    cal.add_component(event)

    # opens file, converts information to ical format, and closes file
    f = open(filepath, 'wb')
    f.write(cal.to_ical())
    f.close()

    # now the ics file has been created at the specified filepath
    # the function doesn't return anything
    return

    #print("created")

# uncomment the following line and run this file to test it. I'd suggest changing the name of the file to make sure you can see what it did.     
# create_ical('test_icals/wood_swallow.ics', 'Softdes Project Test (Wood Swallow)', datetime(2022, 5, 10, 17, 0, 0, 0), datetime(2022, 5, 10, 20, 0, 0, 0), 'ppost@olin.edu')