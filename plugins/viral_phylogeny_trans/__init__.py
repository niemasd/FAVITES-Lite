#! /usr/bin/env python3
from .. import *
from . import coatran
PLUGIN_FUNCTIONS = {
    "Transmission Tree": coatran.coatran_transtree
}
