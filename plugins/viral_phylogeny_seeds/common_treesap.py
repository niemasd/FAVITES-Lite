#! /usr/bin/env python3
from .. import *
from treesap import yule_tree

# sample a seed tree under Yule
def treesap_yule(params, out_fn, verbose=True):
    seeds = [l.split('\t')[1].strip() for l in open(out_fn['transmission_network']) if l.startswith('None\t')]
    tree = yule_tree(1, end_num_leaves=len(seeds))
    for i, node in enumerate(tree.traverse_leaves()):
        node.label = seeds[i]
    tree.write_tree_newick(out_fn['viral_phylogeny_seeds'])
