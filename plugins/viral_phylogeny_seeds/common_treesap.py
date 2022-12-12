#! /usr/bin/env python3
from .. import *
from . import common
from math import *
try:
    from treesap import coalescent_const_pop_tree, dualbirth_tree, nonhomogeneous_yule_tree, yule_tree
except:
    error("Unable to import treesap. Install with: pip install treesap")
try:
    from treeswift import read_tree_newick
except:
    error("Unable to import treeswift. Install with: pip install treeswift")

# sample a seed tree with TreeSAP
def treesap_seed(model, params, out_fn, config, GLOBAL, verbose=True):
    chain_trees = [read_tree_newick(l) for l in open(out_fn['viral_phylogeny_all_chains_time']).read().strip().splitlines()]
    if model == "Coalescent (Neutral)":
        tree = coalescent_const_pop_tree(100., len(chain_trees), continuous=True)
    elif model == "Dual-Birth":
        tree = dualbirth_tree(params['r'], 1., end_num_leaves=len(chain_trees))
    elif model == "Non-Homogeneous Yule":
        tree = nonhomogeneous_yule_tree(lambda t: eval(params['rate_func']), end_num_leaves=len(chain_trees))
    elif model == "Yule":
        tree = yule_tree(1, end_num_leaves=len(chain_trees))
    else:
        error("Invalid TreeSAP model: %s" % model)
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

# model-specific
def treesap_coalescent_const_pop(params, out_fn, config, GLOBAL, verbose=True):
    treesap_seed("Coalescent (Neutral)", params, out_fn, config, GLOBAL, verbose=verbose)
def treesap_dualbirth(params, out_fn, config, GLOBAL, verbose=True):
    treesap_seed("Dual-Birth", params, out_fn, config, GLOBAL, verbose=verbose)
def treesap_nonhom_yule(params, out_fn, config, GLOBAL, verbose=True):
    treesap_seed("Non-Homogeneous Yule", params, out_fn, config, GLOBAL, verbose=verbose)
def treesap_yule(params, out_fn, config, GLOBAL, verbose=True):
    treesap_seed("Yule", params, out_fn, config, GLOBAL, verbose=verbose)
