"""
The ican ical main which ties together the controller, model, and view.
"""

import icanical_controller
import icanical_model
import icanical_view
from send_error_mail import send_error_mail


def main(): # this will probably take a parameter at some point (depending on how we input info to our controller)
    while True:
        # starting the controller makes the bot start waiting for a new email
        controller = icanical_controller.Controller()

        # Once an email is received, try the rest of the code
        try:
            # extract the start time from the email
            start_time = controller.datetimes()[0]
            # extract the end time from the email
            end_time = controller.datetimes()[1]

            # plug in all of the extracted parameters into the model so the view can access them
            event = icanical_model.Model(controller.header, start_time, end_time, controller.recipient)

            # the view uses the extracted parameters so create an ical file
            view = icanical_view.View(event)
            # send an email with the ical attached
            view.send_ical()
        except:
            # if the code fails in any way, send an error email
            send_error_mail(controller.recipient)



if __name__ == "__main__":
    main()
