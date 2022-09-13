#! /usr/bin/env python3
from .. import *
from . import ngg
PLUGIN_FUNCTIONS = {
    "Barabasi-Albert (BA)": ngg.ngg_barabasi_albert,
    "Complete": ngg.ngg_complete,
}
