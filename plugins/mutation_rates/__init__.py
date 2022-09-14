#! /usr/bin/env python3
from .. import *
from . import common_treeswift
PLUGIN_FUNCTIONS = {
    "Autocorrelated Constant Increment": common_treeswift.treeswift_autocorr_const_inc,
    "Constant": common_treeswift.treeswift_constant,
    "None": DUMMY_PLUGIN_FUNC,
}
