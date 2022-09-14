#! /usr/bin/env python3
from .. import *

# sample individuals first time they enter a given state
def state_entry(params, out_fn, mode, verbose=True):
    sampled_states = {s.strip() for s in params['sampled_states'].split(',')}
    if mode in {'first'}:
        sampled_nodes = set()
    else:
        sampled_nodes = None
    sample_times = list() # list of (time, node) tuples
    for line in open(out_fn['all_state_transitions']):
        node, from_s, to_s, t = [v.strip() for v in line.split('\t')]; t = float(t)
        if to_s not in sampled_states:
            continue
        curr_pair = (t, node)
        if mode == 'all':
            sample_times.append(curr_pair)
        elif mode == 'first' and node not in sampled_nodes:
            sample_times.append(curr_pair); sampled_nodes.add(node)
    sample_times.sort()
    f = open(out_fn['sample_times'], 'w')
    for t, node in sample_times:
        f.write("%s\t%s\n" % (node, t))
    f.close()
    if verbose:
        print_log("Sample Times written to: %s" % out_fn['sample_times'])
def state_entry_first(params, out_fn, config, verbose=True):
    state_entry(params, out_fn, "first", verbose=verbose)
def state_entry_all(params, out_fn, config, verbose=True):
    state_entry(params, out_fn, "all", verbose=verbose)
