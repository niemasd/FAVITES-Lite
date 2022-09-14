#! /usr/bin/env python3
from .. import *
from . import specific_time, state_entry, time_windows
PLUGIN_FUNCTIONS = {
    "End": specific_time.end_time,
    "None": DUMMY_PLUGIN_FUNC,
    "Specific Time": specific_time.specific_time,
    "State Entry (All)": state_entry.state_entry_all,
    "State Entry (Initial)": state_entry.state_entry_first,
    "Truncated Exponential": time_windows.time_windows_trunc_expon,
    "Truncated Gamma": time_windows.time_windows_trunc_gamma,
    "Truncated Normal": time_windows.time_windows_trunc_normal,
}
