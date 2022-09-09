#! /usr/bin/env python3
from .. import *
from . import complete
PLUGIN_FUNCTIONS = {
    "Complete": complete.ngg_complete,
}
