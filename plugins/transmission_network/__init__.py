#! /usr/bin/env python3
from .. import *
from . import gemf
PLUGIN_FUNCTIONS = {
    "Granich et al. (2008)": gemf.gemf_favites_granich,
    "Hethcote and Yorke (1984)": gemf.gemf_favites_hethcote_yorke,
    "None": DUMMY_PLUGIN_FUNC,
    "SAPHIRE": gemf.gemf_favites_saphire,
    "Susceptible-Alert-Infected-Susceptible (SAIS)": gemf.gemf_favites_sais,
    "Susceptible-Exposed-Infected-Removed (SEIR)": gemf.gemf_favites_seir,
    "Susceptible-Infected-Removed (SIR)": gemf.gemf_favites_sir,
    "Susceptible-Infected (SI)": gemf.gemf_favites_si,
    "Susceptible-Infected-Susceptible (SIS)": gemf.gemf_favites_sis,
}
