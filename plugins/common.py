#! /usr/bin/env python3
from datetime import datetime
from sys import stderr

# return the current time as a string
def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# print to log (prefixed by current time)
def print_log(s='', end='\n'):
    print("[%s] %s" % (get_time(), s), end=end, file=stderr); stderr.flush()

# print error message
def error(s='', end='\n'):
    print_log(s="ERROR: %s" % s, end=end); exit(1)
