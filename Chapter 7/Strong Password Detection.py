# Chapter 7 Practice Project
# Strong password defined as one with at least 8 characters long, contains both uppercase and lowercase characters
# and has at least one digit.

import re

def strong_password(password: str) -> bool:
    
    if len(password) < 8:
        return False

    strong_password_detector = re.compile(r'''(
        ([a-z]*) # check for lowercase character
        ([A-Z]*) # check for uppercase character
        ([0-9]*) # checks for digits
    )''', re.VERBOSE)

    a = strong_password_detector.search(password)

    for i in a.groups():
        if i == "":
            return False

    return True