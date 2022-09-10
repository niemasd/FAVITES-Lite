#! /usr/bin/env python3
from .. import *
from subprocess import check_output
from treeswift import read_tree_newick

# simulate a coalescent viral phylogeny using CoaTran
def coatran(mode, params, out_fn, verbose=True):
    all_trees = "%s/all_chain_phylogenies.nwk" % out_fn['intermediate']
    if mode == 'transtree':
        command = ['coatran_transtree', out_fn['transmission_network'], out_fn['sample_times']]
    else:
        error("Invalid CoaTran mode: %s" % mode)
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    coatran_out = check_output(command).decode(); f = open(all_trees, 'w'); f.write(coatran_out); f.close()
    trees = [read_tree_newick(l) for l in coatran_out.strip().splitlines()]
    seed_tree = read_tree_newick(out_fn['viral_phylogeny_seeds'])
    seed_tree_leaves = list(seed_tree.traverse_leaves())
    for i in range(len(trees)):
        seed_tree_leaves[i].children.append(trees[i].root)
    seed_tree.suppress_unifurcations()
    seed_tree.write_tree_newick(out_fn['viral_phylogeny_time'])
    if verbose:
        print_log("Viral Phylogeny (Time) written to: %s" % out_fn['viral_phylogeny_time'])

def coatran_transtree(params, out_fn, verbose=True):
    coatran("transtree", params, out_fn, verbose=verbose)
