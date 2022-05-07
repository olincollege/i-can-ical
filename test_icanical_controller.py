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
time_to_tues = abs(1-date.today().weekday())
next_tuesday = date.today().day + time_to_tues
time_to_fri = abs(4-date.today().weekday())
next_friday = date.today().day + time_to_fri


# Test cases
header_no_time = "here is an event"
header_with_time = "Barbecue today at 6"

input_case_no_date_time = (
    [header_no_time, "You're invited!"],
    [header_no_time, "About 4-5 people"], 
    [header_with_time, "This is a message"])
expected_no_date = (False, 
                    False,
                    [datetime(this_year, this_month, today, 18, 0),
                    datetime(this_year, this_month, today, 19, 0)])

input_case_no_time = ( 
    [header_no_time, "Tomorrow"],
    [header_no_time, "January 1st"],
    [header_no_time, "January 1"],
    [header_no_time, "January 1-2"],
    [header_no_time, "01/01/2022"],
    [header_no_time, "1/1/22"])
expected_no_time = (False)

input_case_no_date = (
                    [header_no_time,"Happening at 3"],
                    [header_no_time, "4-5 seats open at 10am"],
                    [header_no_time, "In 6 minutes"],
                    [header_no_time, "From 10-12"])

expected_no_date = (
    [datetime(this_year, this_month, today, 15, 0), 
    datetime(this_year, this_month, today, 15, 0)],
    [datetime(this_year, this_month, today, 10, 0), 
    datetime(this_year, this_month, today, 11, 0)],
    False,
    [datetime(this_year, this_month, today, 10, 0), 
    datetime(this_year, this_month, today, 12, 0)])

input_case_no_period = (
    [header_no_time,"December 12 at 4"],
    [header_no_time, "December 12 at 4"],
    [header_no_time, "December 12 from 11 to 3"])
expected_no_period = (
    [datetime(this_year, 12, 12, 16, 0), 
    datetime(this_year, 12, 12, 17, 0)],\
    [datetime(this_year, 12, 12, 11, 0),\
    datetime(this_year, 12, 12, 15, 0)],
    [datetime(this_year, 12, 12, 12, 0),
    datetime(this_year, 12, 12, 15, 0)],
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
    [header_no_time, "6/15 from 8am to 10am"],
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
    [datetime(this_year, 6, 15, 6, 0),
    datetime(this_year, 6, 15, 8, 0)],
    )
input_relative_time = (
    [header_no_time, "tomorrow at 2pm"],
    [header_no_time, "tomorrow from 11am to 12pm"],
    [header_no_time, "Tuesday at 4pm"],
    [header_no_time,"Friday at 6"],
    [header_no_time, "Today at 4"],
)
expected_relative_time = (
    [datetime(this_year, today+1, 14, 0),
    datetime(this_year, today+1, 15, 0)],
    [datetime(this_year, today+1, 11, 0),
    datetime(this_year, today+1, 12, 0)],
    [datetime(this_year, next_tuesday, 16, 0),
    datetime(this_year, next_tuesday, 17, 0)],
    [datetime(this_year, next_friday, 18, 0),
    datetime(this_year, next_friday, 19, 0)],
    [datetime(this_year, today, 16, 0),
    datetime(this_year, today, 17, 0)],
)

# @pytest.fixture
# def test_cases():
#     return [input_case_no_date_time, input_case_no_time, input_case_no_period,
#             input_case_one_period, input_two_periods, input_relative_time]

# @pytest.fixture
# def expected_outputs():
#     return [expected_no_date, expected_no_time, expected_no_period,
#             expected_one_period, expected_two_periods,
#             expected_relative_time]


# Run test cases
def test_no_date():
    """
    Test the get_date function for cases where no date is given.

    Args:
        input_case_no_date: strings containing no date.
        expected_no_date: expected output of the funtion, False.
    """
    # Create instance of controller
    controller = Controller()
    # Define test cases from test case list
    for i, case in enumerate(input_case_no_date_time):
        # Set header and body attributes (yes, modifying private attributes)
        controller._header = case[0]
        controller._body = case[1]
        result = controller.datetimes()
        assert result == expected_no_date[i]

# def test_no_time(input_case_no_time, expected_no_time):
#     """
#     Test the get_date function for cases where no time is given.

#     Args:
#         input_case_no_time: strings containing no time.
#         expected_no_time: expected output of the funtion, False.
#     """
#     for case in input_case_no_time:
#         assert get_date(case) == expected_no_time

# def test_no_period(input_case_no_period, expected_no_period):
#     """
#     Test the get_date function for cases where no am or pm is given.

#     Args:
#         input_case_no_period: strings containing no am or pm specification.
#         expected_no_period: expected output for each test case, in the form
#             of a list of two strings with start time and end time.
#     """
#     for i, case in enumerate(input_case_no_period):
#         assert get_date(case) == expected_no_period[i]

# def test_one_period(input_case_one_period, expected_one_period):
#     """
#     Test the get_date function for cases where one of the times has an am or
#     pm.

#     Args:
#         input_case_one_period: strings containing only one am or pm.
#         expected_one_period: expected output for each test case, in the form
#             of a list of two strings with start time and end time.
#     """
#     for i, case in enumerate(input_case_one_period):
#         assert get_date(case) == expected_one_period[i]

# def test_two_periods(input_two_periods, expected_two_periods):
#     """
#     Test the get_date function for cases where both start time and end time
#     have an am and pm specified.

#     Args:
#         input_two_periods: strings containing a time range with an am/pm marker
#             on both the start time and end time.
#         expected_two_periods: expected output for each test case, in the form
#             of a list of two strings with start time and end time.
#     """
#     for i, case in enumerate(input_two_periods):
#         assert get_date(case) == expected_two_periods[i]

# def test_relative_time(input_relative_time, expected_relative_time):
#     """
#     Test the get_date function for times that are given in relation to the
#     present date.

#     Args:
#         input_relative_time: strings containing a time in relation to the
#             present date.
#         expected_relative_time: expected output for each test case, in the form
#             of a list of two strings with start time and end time.
#     """
#     for i, case in enumerate(input_relative_time):
#         assert get_date(case) == expected_relative_time[i]