#! /usr/bin/env python3
from .. import *
from . import state_entry
PLUGIN_FUNCTIONS = {
    "State Entry (All)": state_entry.state_entry_all,
    "State Entry (Initial)": state_entry.state_entry_first,
}
