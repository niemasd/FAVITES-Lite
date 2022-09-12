#! /usr/bin/env python3
from .. import *
from . import generate_seq
PLUGIN_FUNCTIONS = {
    "Exact Frequencies": generate_seq.exact_freqs,
}
