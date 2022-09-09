#! /usr/bin/env python3
from .. import *
from . import common_gemf
from os import makedirs
from shutil import copy2
from subprocess import call

# simulate an SIR epidemic using GEMF_FAVITES
def gemf_favites_sir(params, input_cn_fn, output_fn, intermediate_path, verbose=True):
    # set things up
    intermediate_gemf = "%s/GEMF_FAVITES" % intermediate_path; makedirs(intermediate_gemf)
    initial_states_fn = "%s/initial_states.tsv" % intermediate_gemf
    infected_states_fn ="%s/infected_states.txt" % intermediate_gemf
    transition_rates_fn = "%s/transition_rates.tsv" % intermediate_gemf
    gemf_out = "%s/output" % intermediate_gemf

    # run
    common_gemf.gemf_determine_initial_states(params, input_cn_fn, initial_states_fn)
    common_gemf.gemf_write_infected_states("SIR", infected_states_fn)
    common_gemf.gemf_write_transition_rates(params, transition_rates_fn)
    command = [
        'GEMF_FAVITES.py',
        '-c', input_cn_fn,
        '-s', initial_states_fn,
        '-i', infected_states_fn,
        '-r', transition_rates_fn,
        '-t', str(params['duration']),
        '-o', gemf_out,
        '--output_all_transitions',
        '--quiet',
    ]
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    call(command); copy2('%s/transmission_network.txt' % gemf_out, output_fn)
