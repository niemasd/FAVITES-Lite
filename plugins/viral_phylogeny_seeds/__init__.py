#! /usr/bin/env python3
from .. import *
from . import common_treesap
PLUGIN_FUNCTIONS = {
    "None": lambda x=None,y=None,verbose=None: None,
    "Yule": common_treesap.treesap_yule,
}
