"""
Unit tests for the get_date method of the controller class
"""
from datetime import date
from datetime import datetime
from icanical_controller import get_date

this_year = date.today().year
today = date.today().day
time_to_tues = abs(1-date.today().weekday())
next_tuesday = date.today() + time_to_tues
time_to_fri = abs(4-date.today().weekday())
next_friday = date.today() + time_to_fri

# Test cases
input_case_no_date = ("You're invited!", "About 4-5", "This is a message")
expected_no_date = (False)
input_case_no_time = ( 
    "Tomorrow",
    "January 1st",
    "January 1",
    "January 1-2",
    "01/01/2022",
    "1/1/22")
expected_no_time = (False)
input_case_no_period = (
    "December 12 at 4",
    "December 12 at 4",
    "December 12 from 11 to 3")
expected_no_period = (
    [datetime.datetime(this_year, 12, 12, 16, 0), 
    datetime.datetime(this_year, 12, 12, 17, 0)],\
    [datetime.datetime(this_year, 12, 12, 11, 0),\
    datetime.datetime(this_year, 12, 12, 15, 0)],
    [datetime.datetime(this_year, 12, 12, 12, 0),
    datetime.datetime(this_year, 12, 12, 15, 0)],
    )
input_case_one_period = (
    "December 12 from 3-5pm",
    "May 4 from 8am-12"
    "December 12 at 10am",
    "February 6th at 4pm",
)
expected_one_period = (
    [datetime.datetime(this_year, 12, 12, 15, 0),
    datetime.datetime(this_year, 12, 12, 17, 0)],
    [datetime.datetime(this_year, 5, 4, 8, 0),
    datetime.datetime(this_year, 5, 4, 12, 0)],
    [datetime.datetime(this_year, 2, 6, 16, 0),
    datetime.datetime(this_year, 2, 6, 17, 0)],
)
input_two_periods = (
    "January 1st from 10am to 3pm",
    "12/12/22 from 10am 11am",
    "01/01/22 from 8am to 3pm",
    "6/15 from 8am to 10am",
    "May 10 at 6 am to 8 am",
)
expected_two_periods = (
    [datetime.datetime(this_year, 1, 1, 10, 0),
    datetime.datetime(this_year, 1, 1, 15, 0)],
    [datetime.datetime(this_year, 12, 12, 10, 0), 
    datetime.datetime(this_year, 12, 12, 11, 0)],
    [datetime.datetime(this_year, 1, 1, 8, 0),
    datetime.datetime(this_year, 1, 1, 15, 0)],
    [datetime.datetime(this_year, 6, 15, 8, 0),
    datetime.datetime(this_year, 6, 15, 10, 0)],
    [datetime.datetime(this_year, 6, 15, 6, 0),
    datetime.datetime(this_year, 6, 15, 8, 0)],
)
input_relative_time = (
    "tomorrow at 2pm",
    "tomorrow from 11am to 12pm",
    "Tuesday at 4pm",
    "Friday at 6",
    "Today at 4",
)
expected_relative_time = (
    [datetime.datetime(this_year, today+1, 14, 0),
    datetime.dateime(this_year, today+1, 15, 0)],
    [datetime.datetime(this_year, today+1, 11, 0),
    datetime.datetime(this_year, today+1, 12, 0)],
    [datetime.datetime(this_year, next_tuesday, 16, 0),
    datetime.datetime(this_year, next_tuesday, 17, 0)],
    [datetime.datetime(this_year, next_friday, 18, 0),
    datetime.datetime(this_year, next_friday, 19, 0)],
    [datetime.datetime(this_year, today, 16, 0),
    datetime.datetime(this_year, today, 17, 0)],
)

# Run test cases
def test_no_date(input_case_no_date, expected_no_date):
    for case in input_case_no_date:
        assert get_date(case) == expected_no_date

def test_no_time(input_case_no_time, expected_no_time):
    for case in input_case_no_time:
        assert get_date(case) == expected_no_time

def test_no_period(input_case_no_period, expected_no_period):
    for i, case in enumerate(input_case_no_period):
        assert get_date(case) == expected_no_period[i]

def test_one_period(input_case_one_period, expected_one_period):
    for i, case in enumerate(input_case_one_period):
        assert get_date(case) == expected_one_period[i]

def test_two_periods(input_two_periods, expected_two_periods):
    for i, case in enumerate(input_two_periods):
        assert get_date(case) == expected_two_periods[i]

def test_relative_(input_relative_time, expected_relative_time):
    for i, case in enumerate(input_relative_time):
        assert get_date(case) == expected_relative_time[i]