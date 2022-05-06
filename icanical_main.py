"""
The ican ical main which ties together the controller, model, and view.
"""

import icanical_controller
import icanical_model
import icanical_view
from send_error_mail import send_error_mail

def main(): # this will probably take a parameter at some point (depending on how we input info to our controller)
    controller = icanical_controller.Controller()
    try:
        start_time = controller.datetimes()[0]
        end_time = controller.datetimes()[1]
    except:
        send_error_mail(controller.recipient)

    event = icanical_model.Model(controller.header, start_time, end_time, controller.recipient)
    
    view = icanical_view.View(event)
    view.send_ical()

if __name__ == "__main__":
    main()