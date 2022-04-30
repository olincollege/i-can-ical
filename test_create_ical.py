import create_ical
import icalendar
from datetime import datetime

path = '../test_icals/unit_test.ics'

test_case = create_ical.create_ical(path, 'Unit Test', datetime(2022, 4, 27, 17, 0, 0, 0), datetime(2022, 4, 27, 20, 0, 0, 0), 'Dr. Post')

with open(path, 'r') as file:
    text = file.readlines()

desired_output = ['BEGIN:VEVENT\n', 'END:VEVENT\n']

def test_required_contents(): 
    """
    Make sure that the ical includes the begin and end vEvent lines.
    """

    assert desired_output[0] == text[0]
    assert desired_output[1] == text[-1]



#create_ical('/home/igoyal/i-can-ical/test_icals/potato_cannon.ics', 'Potato Cannon', datetime(2022, 4, 27, 17, 0, 0, 0), datetime(2022, 4, 27, 20, 0, 0, 0), 'Dr. Post')