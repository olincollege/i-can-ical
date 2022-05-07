"""
Model of i-can-cal. It holds the attributes of an event, which can then be used
to create and send an ical.
"""

class Model():
    """
    Model that holds event information.

    Attributes:
        _name: a string representing the event's name
        _start_datetime: a datetime object representing the start of the event
        _end_datetime: a datetime object representing the end of the event
        _recipient = a string represting the intended recipient's email address
    """

    def __init__(self, event_name, start_datetime, end_datetime, recipient_email):
        self._name = event_name
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._recipient = recipient_email

    # defined below are a list of properties so that these values can be accessed
    # but not changed by other functions
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
    def recipient(self):
        return self._recipient
