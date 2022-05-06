"""
The view for ican ical.
"""
from create_ical import create_ical
from send_invite import send_invite

class View():
    """
    The view for ican ical draws from the model to create and send an ics file
    to the user.
    """

    def __init__(self, model):
        self._model = model
        
        # all icals will be created at this filepath so that we're not storing
        # icals for old events
        self._filepath = f'test_icals/actual_ical.ics'

    def send_ical(self):
        """
        Creates an ical based on the information in the model object. Then
        sends the ical.
        """
        create_ical(self._filepath, self._model)
        send_invite(self._filepath, self._model)
        print('done')
