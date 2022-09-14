#! /usr/bin/env python3
from .. import *
from random import shuffle, uniform

# random sequence with exact frequencies
def exact_freqs(params, out_fn, config, verbose=True):
    probs = [params['p_%s' % n] for n in 'ACGT']; p_A, p_C, p_G, p_T = probs; k = params['k']
    if not check_props(probs):
        error("Invalid base frequencies: %s" % str({k:params[k] for k in params if k.startswith('p_')}))
    tmp = ['A']*int(k*p_A) + ['C']*int(k*p_C) + ['G']*int(k*p_G)
    tmp += (['T']*(k-len(tmp)))
    shuffle(tmp)
    f = open(out_fn['ancestral_seq'], 'w'); f.write('>Ancestral Sequence (Exact Base Frequencies, k = %s, p_A = %s, p_C = %s, p_G = %s, p_T = %s)\n%s\n' % (k, p_A, p_C, p_G, p_T, ''.join(tmp))); f.close()
    if verbose:
        print_log("Ancestral Sequence written to: %s" % out_fn['ancestral_seq'])

# random sequence with die roll at each position
def seq_die_roll(params, out_fn, config, verbose=True):
    probs = [params['p_%s' % n] for n in 'ACGT']; p_A, p_C, p_G, p_T = probs; k = params['k']
    if not check_props(probs):
        error("Invalid base frequencies: %s" % str({k:params[k] for k in params if k.startswith('p_')}))
    cdf = [p_A, p_A+p_C, p_A+p_C+p_G, 1]; faces = 'ACGT'
    tmp = [None]*k
    for seq_i in range(k):
        num = uniform(0, 1); face_i = 0
        while cdf[face_i] < num:
            face_i += 1
        tmp[seq_i] = faces[face_i]
    f = open(out_fn['ancestral_seq'], 'w'); f.write('>Ancestral Sequence (Base Probabilities, k = %s, p_A = %s, p_C = %s, p_G = %s, p_T = %s)\n%s\n' % (k, p_A, p_C, p_G, p_T, ''.join(tmp))); f.close()
