#! /usr/bin/env python3
from .. import *
from numpy.random import gamma
from random import choice

# sample individuals according to some distribution in their time windows
def time_windows(model, params, out_fn, config, verbose=True):
    end_time = config["Transmission Network"]['param']['duration']
    states_to_sample = {s.strip() for s in params['sampled_states'].split(',')}
    windows = dict() # windows[node] = list of [state, start, end]
    curr_state = dict()
    for l in open(out_fn['all_state_transitions']):
        node, from_s, to_s, t = [v.strip() for v in l.split('\t')]; t = float(t)
        if from_s in states_to_sample:
            windows[node][-1][2] = t
        if to_s in states_to_sample:
            if node not in windows:
                windows[node] = list()
            windows[node].append([to_s, t, end_time])
    f = open(out_fn['sample_times'], 'w')
    for node in windows:
        for _ in range(params['num_samples']):
            state, start, end = choice(windows[node]); length = end - start; delta = None
            if model == "Truncated Gamma":
                for i in range(100): # 100 attempts
                    delta = gamma(params['k'], params['theta']); break
            else:
                error("Model not yet implemented: %s" % model)
            if delta is None:
                error("Failed to generate sample time")
            f.write("%s\t%s\n" % (node, start+delta))
    f.close()

# model-specific functions
def time_windows_trunc_gamma(params, out_fn, config, verbose=True):
    time_windows("Truncated Gamma", params, out_fn, config, verbose=verbose)
