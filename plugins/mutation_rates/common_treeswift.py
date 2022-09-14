#! /usr/bin/env python3
from .. import *
from numpy.random import chisquare, exponential, gamma, lognormal, noncentral_chisquare, noncentral_f, wald
from numpy.random import f as f_dist
from random import random
from treeswift import read_tree_newick

# Autocorrelated Constant Increment
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

# Autocorrelated Exponential
def treeswift_autocorr_exp(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time'])
    for node in tree.traverse_preorder():
        if node.is_root():
            node.rate = params['R0']
        else:
            node.rate = exponential(scale=node.parent.rate)
        if node.edge_length is not None:
            node.edge_length *= node.rate
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Autocorrelated Gamma
def treeswift_autocorr_gamma(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); v = params['v']
    for node in tree.traverse_preorder():
        if node.is_root():
            node.rate = params['R0']
        else:
            scale = v * node.edge_length / node.parent.rate
            shape = node.parent.rate / scale
            node.rate = gamma(shape=shape, scale=scale)
        if node.edge_length is not None:
            node.edge_length *= node.rate
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Autocorrelated Log-Normal
def treeswift_autocorr_lognorm(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); v = params['v']
    for node in tree.traverse_preorder():
        if node.is_root():
            node.rate = params['R0']
        else:
            node.rate = lognormal(mean=node.parent.rate, sigma=v*node.edge_length)
        if node.edge_length is not None:
            node.edge_length *= node.rate
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Constant
def treeswift_constant(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); r = params['rate']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= r
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Chi-Squared
def treeswift_chisq(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); k = params['k']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= chisquare(df=k)
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Exponential
def treeswift_exp(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); b = params['beta']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= exponential(scale=b)
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# F
def treeswift_f_dist(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); d1 = params['d1']; d2 = params['d2']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= f_dist(dfnum=d1, dfden=d2)
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Gamma
def treeswift_gamma(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); k = params['k']; theta = params['theta']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= gamma(shape=k, scale=theta)
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Inverse Gaussian (Wald)
def treeswift_inverse_gaussian(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); mu = params['mu']; lam = params['lambda']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= wald(mean=mu, scale=lam)
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Log-Normal
def treeswift_lognorm(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); mu = params['mu']; sigma = params['sigma']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= lognormal(mean=mu, sigma=sigma)
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Noncentral Chi-Squared
def treeswift_noncentral_chisq(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); k = params['k']; lam = params['lambda']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= noncentral_chisquare(df=k, nonc=lam)
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])

# Noncentral F
def treeswift_noncentral_f(params, out_fn, config, verbose=True):
    tree = read_tree_newick(out_fn['viral_phylogeny_time']); d1 = params['d1']; d2 = params['d2']; lam = params['lambda']
    for node in tree.traverse_preorder():
        if node.edge_length is not None:
            node.edge_length *= noncentral_f(dfnum=d1, dfden=d2, nonc=lam)
    tree.write_tree_newick(out_fn['viral_phylogeny_mut'])
    if verbose:
        print_log("Viral Phylogeny (Mutations) written to: %s" % out_fn['viral_phylogeny_mut'])
