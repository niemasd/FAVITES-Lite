#!/usr/bin/env python3
'''
Calculate pairwise leaf distances from a phylogeny
'''
from os.path import isdir, isfile
from sys import argv
try:
    from treeswift import read_tree_newick
except:
    print("Unable to import TreeSwift. Install via: pip install treeswift"); exit(1)
if len(argv) != 3:
    print("USAGE: %s <input_phylogeny> <output_tsv>" % argv[0]); exit(1)
if not isfile(argv[1]):
    raise ValueError("Input file not found: %s" % argv[1])
if isfile(argv[2]) or isdir(argv[2]):
    raise ValueError("Output file exists: %s" % argv[2])
tree = read_tree_newick(argv[1])
dists = tree.distance_matrix(leaf_labels=True)
labels = list(dists.keys())
out = open(argv[2], 'w'); out.write("ID1\tID2\tDistance\n")
for i in range(len(labels)-1):
    u = labels[i]
    for j in range(i+1, len(labels)):
        v = labels[j]; out.write("%s\t%s\t%s\n" % (u, v, dists[u][v]))
out.close()
