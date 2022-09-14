#! /usr/bin/env python3
from .. import *
from os import stat
from subprocess import call
from treeswift import read_tree_newick

# simulate a coalescent viral phylogeny using CoaTran
def coatran(mode, params, out_fn, config, verbose=True):
    if mode == 'transtree':
        command = ['coatran_transtree', out_fn['transmission_network'], out_fn['sample_times']]
    else:
        error("Invalid CoaTran mode: %s" % mode)
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    f = open(out_fn['viral_phylogeny_all_chains_time'], 'w'); call(command, stdout=f); f.close()
    if stat(out_fn['viral_phylogeny_all_chains_time']).st_size < 2:
        error("CoaTran crashed")
    if verbose:
        print_log("Transmission Chain Viral Phylogenies (Time) written to: %s" % out_fn['viral_phylogeny_all_chains_time'])

def coatran_transtree(params, out_fn, config, verbose=True):
    coatran("transtree", params, out_fn, config, verbose=verbose)
