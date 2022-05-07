import create_ical
import icanical_model
import icalendar
from datetime import datetime

path = '../test_icals/unit_test.ics'

model = icanical_model.Model('Python Unit Testing', datetime(2022, 5, 5, 10),\
     datetime(2022, 5, 5, 11), 'igoyal@olin.edu')
test_case = create_ical.create_ical(path, model)

with open(path, 'r') as file:
    text = file.readlines()

desired_output = ['BEGIN:VCALENDAR\n', 'END:VCALENDAR\n']

def test_vCalendar(): 
    """
    Make sure that the ical includes the begin and end vCalendar lines as the
    start and end of the file.
    """

    assert desired_output[0] == text[0]
    assert desired_output[1] == text[-1]

def test_vEvent():
    """
    Make sure that the ical includes the begin and end vEvent lines.
    """

    assert ('BEGIN:VEVENT\n' in text) == True
    assert ('END:VEVENT\n' in text) == True

def loop_through_ical(word):
    """
    Check if a certain keyword appears anywhere in the ical file.

    This is a helper function for the following unit test.

    Args:
        word: the string being searched for within the file's text.
    """
    for line in text:
        if word in line:
            return True

    return False

def test_key_elements():
    """
    Check that certain information is included in the ics file.

    Searches for key strings in the file using helper function
    loop_through_ical(). Checks for start and end time and that attendee exists.
    """

    assert loop_through_ical('DTSTART') == True
    assert loop_through_ical('DTEND') == True
    assert loop_through_ical('ATTEND') == True
    