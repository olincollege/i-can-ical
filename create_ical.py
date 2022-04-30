"""
Use iCalendar package to create .ics file.
"""

import icalendar as ical
from datetime import datetime # datetime is used when testing this code (currently commented out)

def create_ical(filepath, name, start_datetime, end_datetime, recipient, organizer=None, location=None):
    """
    Take parsed data and turn it into an ical. The ical file will be saved [here].

    Args: 
        filepath: a string specifying the path to where the ics file should be generated.
        name: string representing name or heading of event
        start_datetime: a datetime object specifying the date and time event starts.
        end_datetime:  a datetime specifying the date and time event ends.
        recipient: a string of the recipient's email address
        organizer (optional): string specifying the organizer of the event (often sender
            of the email).
        location (optional): string with the location of the event.
    
    Returns: 
        None
    """

    # you might need to create a calendar object to add the event object to

    # creates an event object
    event = ical.Event()
    event.add('summary', name)
    # converts date and time to standard format. sets timezone as eastern.
    event.add('dtstart', start_datetime)
    event.add('dtend', end_datetime)
    event.add('organizer', organizer)
    event.add('location', ical.vText(location))
    CRLF = '\r\n'
    attendee = ical.vCalAddress(recipient)
    attendee.params['ROLE'] = ical.vText('REQ-PARTICIPANT')
    event.add('attendee', attendee, encode=0)

    f = open(filepath, 'wb')
    f.write(event.to_ical())
    f.close()

# uncomment the following line and run this file to test it. I'd suggest changing the name of the file to make sure you can see what it did.     
create_ical('/home/igoyal/i-can-ical/test_icals/potato_test.ics', 'Potato test', datetime(2022, 4, 27, 17, 0, 0, 0), datetime(2022, 4, 27, 20, 0, 0, 0), 'potatoes@post.com', organizer='Dr. Post')