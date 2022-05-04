"""
The view for ican ical.
"""
from create_ical import create_ical
from send_invite import send_invite

class view():
    """
    The view for ican ical draws from the model to create and send an ics file
    to the user.
    """

    def __init__(self, model):
        self._model = model
        self._filepath = f'test_icals/{model.name}.ics'

    def send_ical(self):
        """
        Creates an ical based on the information in the model object. Then
        sends the ical.
        """
        create_ical()
        send_invite()
        print('done')
