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

    def __init__(self, event_name, start_datetime, end_datetime,\
            recipient_email):
        self._name = event_name
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._recipient = recipient_email

    @property
    def name(self):
        """
        Define property for name. Name is a string representing
        the name of the event.
        """
        return self._name

    @property
    def start(self):
        """
        Define property for start time. Start is a datetime object representing
        the start of the event
        """
        return self._start_datetime

    @property
    def end(self):
        """
        Define property for end time. End is a datetime object representing
        the end of the event
        """
        return self._end_datetime

    @property
    def recipient(self):
        """
        Define property for recipient. Recipient is a string with the email
        address of the attendee who wants to recieve an ical.
        """
        return self._recipient
