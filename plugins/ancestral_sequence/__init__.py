#! /usr/bin/env python3
from .. import *
from . import generate_seq
PLUGIN_FUNCTIONS = {
    "Exact Base Frequencies": generate_seq.exact_freqs,
}
