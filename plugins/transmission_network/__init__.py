#! /usr/bin/env python3
from .. import *
from . import gemf
PLUGIN_FUNCTIONS = {
    "Susceptible-Infected-Removed (SIR)": gemf.gemf_favites_sir,
}
