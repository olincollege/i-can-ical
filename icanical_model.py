"""
Model of i-can-cal. It holds the attributes of an event, which can then be used
to create and send an ical.
"""

class Model():
    """
    Model that holds event information.

    Attributes:

    """

    def __init__(self, event_name, start_datetime, end_datetime, attendee_email, organizer_email=None, location=None):
        self._name = event_name
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._attendee = attendee_email
        self._organizer = organizer_email
        self._location = location

    # defined below are a list of properties so that these values can be accessed but not changed by other functions
    @property
    def name(self):
        return self._name

    @property
    def start(self):
        return self._start_datetime

    @property
    def end(self):
        return self._end_datetime
    
    @property
    def attendee(self):
        return self._attendee

    @property
    def organizer(self):
        return self._organizer

    @property
    def location(self):
        return self._location
    