#! /usr/bin/env python3
from .. import *
from . import common_treeswift
PLUGIN_FUNCTIONS = {
    "Autocorrelated Constant Increment": common_treeswift.treeswift_autocorr_const_inc,
    "Autocorrelated Exponential": common_treeswift.treeswift_autocorr_exp,
    "Autocorrelated Gamma": common_treeswift.treeswift_autocorr_gamma,
    "Autocorrelated Log-Normal": common_treeswift.treeswift_autocorr_lognorm,
    "Chi-Squared": common_treeswift.treeswift_chisq,
    "Constant": common_treeswift.treeswift_constant,
    "Exponential": common_treeswift.treeswift_exp,
    "F": common_treeswift.treeswift_f_dist,
    "Gamma": common_treeswift.treeswift_gamma,
    "Inverse Gaussian (Wald)": common_treeswift.treeswift_inverse_gaussian,
    "Log-Normal": common_treeswift.treeswift_lognorm,
    "None": DUMMY_PLUGIN_FUNC,
}
