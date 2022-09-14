#! /usr/bin/env python3
from .. import *
from os import stat
from subprocess import call
from treeswift import read_tree_newick

# run seq-gen
def seqgen(mode, params, out_fn, config, verbose=True):
    treestr = open(out_fn['viral_phylogeny_mut']).read().strip().replace('[&R] ','')
    if ',' not in treestr: # if one-node tree, add DUMMY 0-length leaf
        treestr = "(DUMMY:0,%s);" % treestr.replace('(','').replace(')','')[:-1]
    else: # otherwise, resolve polytomies and unifurcations
        tmp = read_tree_newick(treestr)
        tmp.suppress_unifurcations(); tmp.resolve_polytomies()
        for node in tmp.traverse_internal(): # remove internal node labels
            node.label = None
        treestr = tmp.newick().replace('[&R] ','').strip()
    root_seq = ''.join(l.strip() for l in open(out_fn['ancestral_seq']) if not l.startswith('>'))
    seqgen_tree_fn = "%s/seqgen.phy" % out_fn['intermediate']
    seqgen_log_fn = "%s/seqgen.log" % out_fn['intermediate']
    f = open(seqgen_tree_fn, 'w'); f.write("1 %d\nROOT %s\n1\n%s" % (len(root_seq),root_seq,treestr)); f.close()
    command = ['seq-gen', '-of', '-k1']
    if mode in {'GTR', 'GTR+G'}: # add model
        command += ['-m', 'GTR']
    if mode in {'GTR', 'GTR+G'}: # add base frequencies
        command += (['-f'] + [str(params['p_%s' % n]) for n in 'ACGT'])
    if mode in {'GTR', 'GTR+G'}: # add GTR transition rates
        command += (['-r'] + [str(params['r_%s-%s' % tuple(pair)]) for pair in ['AC', 'AG', 'AT', 'CG', 'CT', 'GT']])
    if mode in {'GTR', 'GTR+G'}: # add proportion invariable
        command += ['-i', str(params['prop_invariable'])]
    if mode in {'GTR+G'}: # add Gamma parameters
        command += ['-a', str(params['alpha'])]
        if params['num_cats'] > 0:
            command += ['-g', str(params['num_cats'])]
    command += [seqgen_tree_fn]
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    out_f = open(out_fn['sequences'], 'w'); log_f = open(seqgen_log_fn, 'w'); call(command, stdout=out_f, stderr=log_f); log_f.close(); out_f.close()
    if stat(out_fn['sequences']).st_size < 2:
        error("Seq-Gen crashed. See log file: %s" % seqgen_log_fn)
    if verbose:
        print_log("Sequences written to: %s" % out_fn['sequences'])

# model-specific functions
def seqgen_gtr(params, out_fn, config, verbose=True):
    seqgen("GTR", params, out_fn, config, verbose=verbose)
def seqgen_gtr_gamma(params, out_fn, config, verbose=True):
    seqgen("GTR+G", params, out_fn, config, verbose=verbose)
