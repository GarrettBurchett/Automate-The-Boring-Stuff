# Chapter 7 Practice Project
# Write a regular expression that can detect dates in the DD/MM/YYYY format.
# Assumptions: Days range from 01 to 31, Months range from 01 to 12, and Years range from 1000 to 2999

import re

detect_date = re.compile(r'''(
    ([0-3]\d{1})        # Days
    (/|-)?              # separator
    ([0-1]\d{1})        # Months
    (/|-)?              # separator
    ([1-2]\d{3})        # Year
)''', re.VERBOSE)

def is_leap_year(year: int) -> bool:
    ''' Check whether a given year is a leap year or not.'''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    return False

def is_valid_date(month: int, day: int, year: int) -> bool:
    ''' Checks whether a given date is a valid date or not'''
    if month == 2 and day == 29 and is_leap_year(year):
        return True
    elif month == 2 and day <= 28:
        return True
    elif day == 31 and month in [1, 3, 5, 7, 8, 10, 12]:
        return True
    elif day <= 30 and month <= 12 and month != 2:
        return True

    return False

test_phrase = 'Some words before a date 30/04/2022. Some more words before another date 31/03/2022.Testing 42/08/1750 31/02/1991 20/03/3000 15/10/1862 29/02/2004 29/02/1997 15/15/1515 23/24/2400'

# Find all of the dates in the test_phrase variable
found_dates = detect_date.findall(test_phrase)

# Create a variable that creates a tuple of the month(MM), day(DD), and year(YYYY) from each date in found_dates
# found_dates returns ('DD/MM/YYYY', 'DD', '/', 'MM', '/', 'YYYY')
dates = zip([date[3] for date in found_dates], 
            [date[1] for date in found_dates], 
            [date[5] for date in found_dates])

# Now print the date that was found and whether it is a valid date or not
# dates returns ('MM', 'DD', 'YYYY') which are all strings
for date in list(dates):
    print(date, is_valid_date(int(date[0]), int(date[1]), int(date[2])))