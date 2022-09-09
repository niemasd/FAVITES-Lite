#! /usr/bin/env python3
from .. import *
from . import ngg
PLUGIN_FUNCTIONS = {
    "Complete": ngg.ngg_complete,
}
