#! /usr/bin/env python3
from .. import *
from . import coatran
PLUGIN_FUNCTIONS = {
    "Infection Time": coatran.coatran_inftime,
    "None": DUMMY_PLUGIN_FUNC,
    "Transmission Tree": coatran.coatran_transtree
}
