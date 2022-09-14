#! /usr/bin/env python3
from .. import *
from . import seqgen
PLUGIN_FUNCTIONS = {
    "General Time-Reversible (GTR)": seqgen.seqgen_gtr,
    "None": DUMMY_PLUGIN_FUNC,
}
