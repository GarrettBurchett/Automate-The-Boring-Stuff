# Chapter 7 Practice Project

import re

def strip_regex(entry: str) -> str:

    strip = re.compile(r'''(^\s*)(\S*)(\s)*$''')
    stripped_string = strip.search(entry)
    
    return stripped_string.group(2)

print(strip_regex('  Hello! '))