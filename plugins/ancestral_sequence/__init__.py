#! /usr/bin/env python3
from .. import *
from . import generate_seq
PLUGIN_FUNCTIONS = {
    "Base Probabilities": generate_seq.seq_die_roll,
    "Exact Base Frequencies": generate_seq.exact_freqs,
    "None": lambda x=None,y=None,verbose=None: None,
}
