#! /usr/bin/env python3
from .. import *
from . import sir
PLUGIN_FUNCTIONS = {
    "Susceptible-Infected-Removed (SIR)": sir.gemf_favites_sir,
}
