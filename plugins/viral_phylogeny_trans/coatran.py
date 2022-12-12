#! /usr/bin/env python3
from .. import *
from os import stat
from subprocess import call
try:
    from treeswift import read_tree_newick
except:
    error("Unable to import treeswift. Install with: pip install treeswift")

# simulate a coalescent viral phylogeny using CoaTran
def coatran(exe, params, out_fn, config, verbose=True):
    if exe in {'coatran_inftime', 'coatran_transtree'}:
        command = [exe, out_fn['transmission_network'], out_fn['sample_times']]
    elif exe == 'coatran_constant':
        command = [exe, out_fn['transmission_network'], out_fn['sample_times'], str(params['N'])]
    else:
        error("Invalid CoaTran exe: %s" % exe)
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    f = open(out_fn['viral_phylogeny_all_chains_time'], 'w'); call(command, stdout=f); f.close()
    if stat(out_fn['viral_phylogeny_all_chains_time']).st_size < 2:
        error("CoaTran crashed")
    if verbose:
        print_log("Transmission Chain Viral Phylogenies (Time) written to: %s" % out_fn['viral_phylogeny_all_chains_time'])

# model-specific plugins
def coatran_constant(params, out_fn, config, verbose=True):
    coatran("coatran_constant", params, out_fn, config, verbose=verbose)
def coatran_inftime(params, out_fn, config, verbose=True):
    coatran("coatran_inftime", params, out_fn, config, verbose=verbose)
def coatran_transtree(params, out_fn, config, verbose=True):
    coatran("coatran_transtree", params, out_fn, config, verbose=verbose)
