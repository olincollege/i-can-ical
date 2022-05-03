from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Path

cal = Calendar()
cal.add('attendee', 'MAILTO:igoyal@olin.edu')

event = Event()
event.add('summary', 'Python meeting about calendaring')
event.add('dtstart', datetime(2022, 5, 4, 8, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2022, 5, 4, 10, 0, 0, tzinfo=pytz.utc))
event.add('dtstamp', datetime(2022, 10, 24, 0, 10, 0, tzinfo=pytz.utc))

organizer = vCalAddress('MAILTO:oclavering@olin.edu')
organizer.params['cn'] = vText('Sir Jon')
organizer.params['role'] = vText('CEO')
event['organizer'] = organizer
event['location'] = vText('London, UK')

# Adding events to calendar
cal.add_component(event)

directory = str(Path('test_icals/magnolia_tree').parent.parent) + "/"
print("ics file will be generated at ", directory)
f = open(os.path.join(directory, 'example.ics'), 'wb')
f.write(cal.to_ical())
f.close()