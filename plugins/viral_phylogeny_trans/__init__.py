#! /usr/bin/env python3
from .. import *
from . import coatran
PLUGIN_FUNCTIONS = {
    "Constant Effective Population Size": coatran.coatran_constant,
    "Infection Time": coatran.coatran_inftime,
    "None": DUMMY_PLUGIN_FUNC,
    "Transmission Tree": coatran.coatran_transtree
}
