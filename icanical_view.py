"""
The view for ican ical.
"""

class view():
    """
    The view for ican ical draws from the model to create and send an ics file
    to the user.
    """

    def __init__(self, model):
        self._model = model
        self._filepath = f'test_icals/{model.name}.ics'

    def send_ical(self):
        pass
    # put in the other two functions and also change their inputs.
