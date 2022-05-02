"""
Unit tests for the get_date method of the controller class
"""
from datetime import date
from datetime import datetime

# Test cases
input_case_no_date = ("You're invited!", "About 4-5", "This is a message")
expected_no_date = (False)
input_case_no_time = ("Tomorrow", "January 1st", "January 1", "January 1-2",\
     "01/01/2022", "1/1/22")
expected_no_time = (False)
input_case_no_period = ("December 12 at 4", "December 12 at 4",\
     "Tomorrow at 6", "Thursday from 8-9", "December 12 from 11 to 3")
expected_no_period = ([datetime.datetime(2022, 12, 12, 16, 0), \
                    datetime.datetime(2022, 12, 12, 17, 0)],\
                      [datetime.datetime(2022, 12, 12, 11, 0),\
                    datetime.datetime(2022, 12, 12, 15, 0)],)\