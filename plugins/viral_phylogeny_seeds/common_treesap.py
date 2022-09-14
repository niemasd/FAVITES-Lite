#! /usr/bin/env python3
from .. import *
from . import common
from treesap import yule_tree
from treeswift import read_tree_newick

# sample a seed tree under Yule
def treesap_yule(params, out_fn, config, verbose=True):
    chain_trees = [read_tree_newick(l) for l in open(out_fn['viral_phylogeny_all_chains_time']).read().strip().splitlines()]
    tree = yule_tree(1, end_num_leaves=len(chain_trees))
    tree.scale_edges(params['height']/tree.height())
    for i, node in enumerate(tree.traverse_leaves()):
        node.label = str(i)
    tree.write_tree_newick(out_fn['viral_phylogeny_seed_time'])
    if verbose:
        print_log("Seed Viral Phylogeny (Time) written to: %s" % out_fn['viral_phylogeny_all_chains_time'])
    common.merge_trees(tree, chain_trees)
    tree.write_tree_newick(out_fn['viral_phylogeny_time'])
    if verbose:
        print_log("Viral Phylogeny (Time) written to: %s" % out_fn['viral_phylogeny_time'])
