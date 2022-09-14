#! /usr/bin/env python3
from .. import *
from treeswift import read_tree_newick

# constant mutation rate
def treeswift_constant(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time'])
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= params['rate']
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])
