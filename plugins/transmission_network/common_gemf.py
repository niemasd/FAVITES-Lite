#! /usr/bin/env python3
from .. import *
from random import choice

# determine initial states
def gemf_determine_initial_states(params, input_cn_fn, initial_states_fn):
    state_counts = {p[2:].strip():params[p] for p in params if p.startswith('N_')}
    nonzero_states = [p for p,c in state_counts.items() if c != 0]; state_counts_sum = sum(state_counts.values())
    nodes = [l.split('\t')[1].strip() for l in open(input_cn_fn) if l.startswith('NODE')]
    if state_counts_sum != len(nodes):
        error("Contact network has %d nodes, but total of state counts is: %d" % (len(nodes), state_counts_sum))
    f = open(initial_states_fn, 'w')
    for node in nodes:
        state = choice(nonzero_states); state_counts[state] -= 1
        if state_counts[state] == 0:
            nonzero_states.remove(state)
        f.write("%s\t%s\n" % (node, state))
    f.close()

# write infected states
def gemf_write_infected_states(model, infected_states_fn):
    infected_states = {
        "SIR": ['I'],
    }
    if model not in infected_states:
        error("Invalid GEMF model: %s" % model)
    f = open(infected_states_fn, 'w')
    for s in infected_states[model]:
        f.write('%s\n' % s)
    f.close()

# write transition rates
def gemf_write_transition_rates(params, transition_rates_fn):
    f = open(transition_rates_fn, 'w')
    for p in params:
        if not p.startswith('R_'):
            continue
        parts = [s.strip() for s in p[2:].replace('-','_').split('_')]
        if len(parts) == 2:
            parts.append(None)
        parts.append(params[p])
        f.write("%s\t%s\t%s\t%s\n" % tuple(parts))
    f.close()
