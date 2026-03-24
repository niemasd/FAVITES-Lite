#! /usr/bin/env python3
# standard imports
from datetime import datetime
from sys import stderr
import math

# constants
ZERO_THRESH = 0.00000000001
LOG_FILES = list()

# non-standard imports
try:
    from scipy.stats import truncnorm
except:
    error("Unable to import scipy. Install with: pip install scipy")

# dummy plugin function
def DUMMY_PLUGIN_FUNC(params, out_fn, config, GLOBAL, verbose=True):
    pass

# return the current time as a string
def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# print to log (prefixed by current time)
def print_log(s='', end='\n'):
    t = "[%s] %s" % (get_time(), s)
    for f in LOG_FILES:
        print(t, end=end, file=f); f.flush()

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

# sample from a truncated normal distribution with (non-truncated) mean `loc` and (non-truncated) stdev `scale` in range [`a`,`b`]
# I'm using the Wikipedia notation: https://en.wikipedia.org/wiki/Truncated_normal_distribution
# SciPy's `truncnorm` defines `a` and `b` as "standard deviations above/below `loc`", so I need to convert
def truncnorm_rvs(loc, scale, a_min, b_max, size):
    a = (a_min - loc) / scale
    b = (b_max - loc) / scale
    return truncnorm.rvs(a=a, b=b, loc=loc, scale=scale, size=size)
