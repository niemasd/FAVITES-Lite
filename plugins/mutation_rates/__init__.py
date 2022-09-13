#! /usr/bin/env python3
from .. import *
from . import constant
PLUGIN_FUNCTIONS = {
    "Constant": constant.treeswift_constant,
    "None": lambda x=None,y=None,verbose=None: None,
}
