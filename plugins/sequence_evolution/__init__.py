#! /usr/bin/env python3
from .. import *
from . import seqgen
PLUGIN_FUNCTIONS = {
    "General Time-Reversible (GTR)": seqgen.seqgen_gtr,
    "General Time-Reversible (GTR) + Codon": seqgen.seqgen_gtr_codon,
    "General Time-Reversible (GTR) + Gamma": seqgen.seqgen_gtr_gamma,
    "None": DUMMY_PLUGIN_FUNC,
}
