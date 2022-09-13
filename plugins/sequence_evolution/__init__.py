#! /usr/bin/env python3
from .. import *
from . import seqgen
PLUGIN_FUNCTIONS = {
    "General Time-Reversible (GTR)": seqgen.seqgen_gtr,
    "None": lambda x=None,y=None,verbose=None: None,
}
