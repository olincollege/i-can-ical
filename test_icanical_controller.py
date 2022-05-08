"""
Unit tests for the get_date method of the controller class.
"""
import io
import pytest
from datetime import date
from datetime import datetime
from icanical_controller import get_date
from icanical_controller import Controller

this_year = date.today().year
this_month = date.today().month
today = date.today().day


# Test cases
header_no_time = "here is an event"
header_with_time = "Barbecue today at 6"

input_case_no_date_time = (
    [header_no_time, "You're invited!"],
    [header_with_time, "This is a message"])
expected_no_date_time = (False, 
                    [datetime(this_year, this_month, today, 18, 0),
                    datetime(this_year, this_month, today, 19, 0)])

input_case_no_time = ( 
    [header_no_time, "Tomorrow"],
    [header_no_time, "January 1st"],
    [header_no_time, "January 1"],
    [header_no_time, "January 1 thru 2"],
    [header_no_time, "01/01/2022"],
    [header_no_time, "1/1/22"])
expected_no_time = (False)

input_case_no_date = (
                    [header_no_time,"Happening at 3"],
                    [header_no_time, "In 6 minutes"],
                    [header_no_time, "At 11am"]) # Assuming this test is not run before 5am

expected_no_date = (
    [datetime(this_year, this_month, today, 15, 0), 
    datetime(this_year, this_month, today, 16, 0)],
    False,
    [datetime(this_year, this_month, today, 11, 0), 
    datetime(this_year, this_month, today, 12, 0)])

input_case_no_period = (
    [header_no_time,"December 12th at 4"],
    [header_no_time, "December 12 at 11"],
    [header_no_time, "December 12 from 10-2"])
expected_no_period = (
    [datetime(this_year, 12, 12, 16, 0),
    datetime(this_year, 12, 12, 17, 0)],
    [datetime(this_year, 12, 12, 23, 0),
    datetime(this_year, 12, 13, 0, 0)],
    [datetime(this_year, 12, 12, 10, 0),
    datetime(this_year, 12, 12, 14, 0)],
    )

input_case_one_period = (
    [header_no_time, "December 12 from 3-5pm"],
    [header_no_time, "May 31 from 8am-12"],
    [header_no_time, "December 12 at 10am"],
    [header_no_time, "February 6th at 4pm"],
    )
expected_one_period = (
    [datetime(this_year, 12, 12, 15, 0),
    datetime(this_year, 12, 12, 17, 0)],
    [datetime(this_year, 5, 31, 8, 0),
    datetime(this_year, 5, 31, 12, 0)],
    [datetime(this_year, 12, 12, 10, 0),
    datetime(this_year, 12, 12, 11, 0)],
    [datetime(this_year, 2, 6, 16, 0),
    datetime(this_year, 2, 6, 17, 0)],
    )
input_two_periods = (
    [header_no_time, "January 1st from 10am to 3pm"],
    [header_no_time, "12/12/22 from 10am 11am"],
    [header_no_time, "01/01/22 from 8am to 3pm"],
    [header_no_time, "6/15 from 8:00am to 10:00am"],
    [header_no_time, "May 10 at 6 am to 8 am"],
    )
expected_two_periods = (
    [datetime(this_year, 1, 1, 10, 0),
    datetime(this_year, 1, 1, 15, 0)],
    [datetime(this_year, 12, 12, 10, 0),
    datetime(this_year, 12, 12, 11, 0)],
    [datetime(this_year, 1, 1, 8, 0),
    datetime(this_year, 1, 1, 15, 0)],
    [datetime(this_year, 6, 15, 8, 0),
    datetime(this_year, 6, 15, 10, 0)],
    [datetime(this_year, 5, 10, 6, 0),
    datetime(this_year, 5, 10, 8, 0)],
    )
input_relative_time = (
    [header_no_time, "tomorrow at 2pm"],
    [header_no_time, "tomorrow from 11am to 12pm"],
    [header_no_time, "Today at 4"],
)
expected_relative_time = (
    [datetime(this_year, this_month, today+1, 14, 0),
    datetime(this_year, this_month, today+1, 15, 0)],
    [datetime(this_year, this_month, today+1, 11, 0),
    datetime(this_year, this_month, today+1, 12, 0)],
    [datetime(this_year, this_month, today, 16, 0),
    datetime(this_year, this_month, today, 17, 0)],
)


# Run test cases
def test_no_date_no_time():
    """
    Test the datetimes method for cases where no date or time is given in the
    body of the email. Also check if a time in the header is detected.
    """
    # Create instance of controller
    controller = Controller()
    # Define test cases from test case list
    for i, case in enumerate(input_case_no_date_time):
        # Set header and body attributes (yes, modifying private attributes)
        controller._header = case[0]
        controller._body = case[1]
        result = controller.datetimes()
        assert result == expected_no_date_time[i]

def test_no_time():
    """
    Test the datetimes method for cases where no time is given in the
    body or header of the email. 
    """
    # Create instance of controller
    controller = Controller()
    # Define test cases from test case list
    for case in input_case_no_time:
        # Set header and body attributes (yes, modifying private attributes)
        controller._header = case[0]
        controller._body = case[1]
        result = controller.datetimes()
        assert result == expected_no_time

def test_no_date():
    """
    Test the datetimes method for cases where no date or time is given in the
    body of the email.
    """
    # Create instance of controller
    controller = Controller()
    # Define test cases from test case list
    for i, case in enumerate(input_case_no_date):
        # Set header and body attributes (yes, modifying private attributes)
        controller._header = case[0]
        controller._body = case[1]
        result = controller.datetimes()
        assert result == expected_no_date[i]

def test_no_period():
    """
    Test the datetimes method for cases where no am or pm is given in the
    body or header of the email.
    """
    # Create instance of controller
    controller = Controller()
    # Define test cases from test case list
    for i, case in enumerate(input_case_no_period):
        # Set header and body attributes (yes, modifying private attributes)
        controller._header = case[0]
        controller._body = case[1]
        result = controller.datetimes()
        assert result == expected_no_period[i]

def test_one_period():
    """
    Test the datetimes method for cases where one am or pm is given in the
    body of the email.
    """
    # Create instance of controller
    controller = Controller()
    # Define test cases from test case list
    for i, case in enumerate(input_case_one_period):
        # Set header and body attributes (yes, modifying private attributes)
        controller._header = case[0]
        controller._body = case[1]
        result = controller.datetimes()
        assert result == expected_one_period[i]

def test_two_periods():
    """
    Test the datetimes method for cases where am or pm is given for both itmer
    in a range in the body of the email.
    """
    # Create instance of controller
    controller = Controller()
    # Define test cases from test case list
    for i, case in enumerate(input_two_periods):
        # Set header and body attributes (yes, modifying private attributes)
        controller._header = case[0]
        controller._body = case[1]
        result = controller.datetimes()
        assert result == expected_two_periods[i]

def test_relative_time():
    """
    Test the datetimes method for cases where a time is given that is relative
    to the current date, such as 'tomorrow'. 
    """
    # Create instance of controller
    controller = Controller()
    # Define test cases from test case list
    for i, case in enumerate(input_relative_time):
        # Set header and body attributes (yes, modifying private attributes)
        controller._header = case[0]
        controller._body = case[1]
        result = controller.datetimes()
        assert result == expected_relative_time[i]