#! /usr/bin/env python3
from .. import *
from . import ngg
PLUGIN_FUNCTIONS = {
    "Barabasi-Albert (BA)": ngg.ngg_barabasi_albert,
    "Barbell": ngg.ngg_barbell,
    "Complete": ngg.ngg_complete,
    "Cycle": ngg.ngg_cycle,
    "Empty": ngg.ngg_empty,
}
