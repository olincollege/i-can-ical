"""
The ican ical main which ties together the controller, model, and view.
"""

import icanical_controller
import icanical_model
import icanical_view

def __main__(recipient, location=None): # this will probably take a parameter at some point (depending on how we input info to our controller)
    controller = icanical_controller.Controller()
    start_time = controller.datetimes()[0]
    end_time = controller.datetimes()[1]

    model = icanical_model.Model(controller.header(), start_time, end_time, recipient, controller.sender(), location=location)
    
    view = icanical_view.View(model)
    view.send_ical()
