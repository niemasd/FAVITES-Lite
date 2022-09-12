#! /usr/bin/env python3
from datetime import datetime
from sys import stderr
ZERO_THRESH = 0.000001

# return the current time as a string
def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# print to log (prefixed by current time)
def print_log(s='', end='\n'):
    print("[%s] %s" % (get_time(), s), end=end, file=stderr); stderr.flush()

# print error message
def error(s='', end='\n'):
    print_log(s="ERROR: %s" % s, end=end); exit(1)

# check that proportions/probabilities add up to 1
def check_props(props):
    tot = 0
    for p in props:
        if p < 0 or p > 1:
            return False
        tot += p
    return abs(tot - 1) <= ZERO_THRESH
