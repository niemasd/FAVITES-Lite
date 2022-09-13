#! /usr/bin/env python3
from .. import *
from . import gemf
PLUGIN_FUNCTIONS = {
    "None": lambda x=None,y=None,verbose=None: None,
    "Susceptible-Infected-Removed (SIR)": gemf.gemf_favites_sir,
}
