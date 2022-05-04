"""
Use iCalendar package to create .ics file.
"""

import icalendar as ical
from datetime import datetime # datetime is used when testing this code (currently commented out)
import icanical_model

# replaced all these parameters with model. if it doesn't end up working, just change them back. parameters: , name, start_datetime, end_datetime, recipient, organizer_email=None, location=None
def create_ical(filepath, model):
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
    # pulls information from the model and sets them to convenient variables
    name = model.name()
    start_datetime = model.start()
    end_datetime = model.end()
    recipient = model.attendee()
    organizer_email = model.organizer()
    location = model.location()


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

    organizer = ical.vCalAddress(organizer_email) # consider the case where there is no organizer (what happens if organizer_address = None?)
    event['organizer'] = organizer
    event['location'] = ical.vText(location)

    # sets recipient/attendee
    attendee = ical.vCalAddress(recipient)
    attendee.params['ROLE'] = ical.vText('REQ-PARTICIPANT')
    event.add('attendee', attendee, encode=0)

    # adds event to calendar
    cal.add_component(event)

    # converts information to ical format
    f = open(filepath, 'wb')
    f.write(cal.to_ical())
    f.close()

    print("created")

# uncomment the following line and run this file to test it. I'd suggest changing the name of the file to make sure you can see what it did.     
create_ical('test_icals/wood_swallow.ics', 'Softdes Project Test (Wood Swallow)', datetime(2022, 5, 10, 17, 0, 0, 0), datetime(2022, 5, 10, 20, 0, 0, 0), 'ppost@olin.edu', organizer_email='Dr. Post')