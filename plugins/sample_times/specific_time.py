#! /usr/bin/env python3
from .. import *

# sample individuals at a specific time
def specific_time(params, out_fn, config, verbose=True):
    states_to_sample = {s.strip() for s in params['sampled_states'].split(',')}
    nodes_to_sample = set()
    for l in open(out_fn['all_state_transitions']):
        node, from_s, to_s, t = [v.strip() for v in l.split('\t')]; t = float(t)
        if t > params['sample_time']:
            break
        if to_s in states_to_sample:
            nodes_to_sample.add(node)
        else:
            nodes_to_sample.discard(node)
    f = open(out_fn['sample_times'], 'w')
    for node in nodes_to_sample:
        f.write("%s\t%s\n" % (node, params['sample_time']))
    f.close()
    if verbose:
        print_log("Sample Times written to: %s" % out_fn['sample_times'])
