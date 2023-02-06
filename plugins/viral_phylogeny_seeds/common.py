#! /usr/bin/env python3
from .. import *
try:
    from treeswift import Tree
except:
    error("Unable to import treeswift. Install with: pip install treeswift")

# merge seed tree and transmission chain trees
def merge_trees(seed_tree, transmission_chain_trees):
    if not isinstance(seed_tree, Tree):
        error("Seed phylogeny must be treeswift.Tree object")
    for tree in transmission_chain_trees:
        if not isinstance(tree, Tree):
            error("All transmission chain phylogenies must be treeswift.Tree objects")
    seed_tree_leaves = list(seed_tree.traverse_leaves())
    for i in range(len(seed_tree_leaves)):
        seed_tree_leaves[i].children.append(transmission_chain_trees[i].root)
    seed_tree.suppress_unifurcations()
