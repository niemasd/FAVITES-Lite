#! /usr/bin/env python3
from .. import *
from . import coatran
PLUGIN_FUNCTIONS = {
    "None": lambda x=None,y=None,verbose=None: None,
    "Transmission Tree": coatran.coatran_transtree
}
