#! /usr/bin/env python3
from .. import *
from random import random
from treeswift import read_tree_newick

# Autocorrelated Constant Increment mutation rates
def treeswift_autocorr_const_inc(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time'])
    p = params['p']; p_over_2 = p/2; delta = params['delta']; R_min = params['R_min']; R_max = params['R_max']
    for node in tree.traverse_preorder():
        if node.is_root():
            node.rate = params['R0']
        else:
            node.rate = node.parent.rate; tmp = random()
            if tmp <= p_over_2:
                node.rate += delta
                if node.rate > R_max:
                    node.rate = R_max
            elif tmp <= p:
                node.rate -= delta
                if node.rate < R_min:
                    node.rate = R_min
        if node.edge_length is not None:
            node.edge_length *= node.rate
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Constant mutation rates
def treeswift_constant(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); r = params['rate']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= r
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])
