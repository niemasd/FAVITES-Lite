#! /usr/bin/env python3
from .. import *
from . import common_treesap
PLUGIN_FUNCTIONS = {
    "None": DUMMY_PLUGIN_FUNC,
    "Yule": common_treesap.treesap_yule,
}
