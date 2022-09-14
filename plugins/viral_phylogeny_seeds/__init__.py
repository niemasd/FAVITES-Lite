#! /usr/bin/env python3
from .. import *
from . import common_treesap
PLUGIN_FUNCTIONS = {
    "Dual-Birth": common_treesap.treesap_dualbirth,
    "None": DUMMY_PLUGIN_FUNC,
    "Yule": common_treesap.treesap_yule,
}
