# Chapter 7 Practice Project
# Strong password defined as one with at least 8 characters long, contains both uppercase and lowercase characters
# and has at least one digit.

import re

strong_password_detector = re.compile(r'''(
    [a-z]* # check for lowercase character
    [A-Z]* # check for uppercase character
    [0-9]* # checks for digits
)''', re.VERBOSE)

def strong_password(password: str) -> bool:
    return pass