#! /usr/bin/env python3
from .. import *
from . import specific_time, state_entry
PLUGIN_FUNCTIONS = {
    "None": lambda x=None,y=None,verbose=None: None,
    "Specific Time": specific_time.specific_time,
    "State Entry (All)": state_entry.state_entry_all,
    "State Entry (Initial)": state_entry.state_entry_first,
}
