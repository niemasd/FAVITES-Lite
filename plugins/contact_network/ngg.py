#! /usr/bin/env python3
from .. import *
from subprocess import call

# simulate contact network using NiemaGraphGen
def ngg(exe, params, out_fn, verbose=True):
    if exe == 'ngg_barabasi_albert':
        command = ['ngg_barabasi_albert', str(params['n']), str(params['m'])]
    elif exe == 'ngg_complete':
        command = ['ngg_complete', str(params['n'])]
    else:
        error("Invalid NiemaGraphGen exe: %s" % exe)
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    f = open(out_fn['contact_network'], 'w'); call(command, stdout=f); f.close()
    if verbose:
        print_log("Contact Network written to: %s" % out_fn['contact_network'])
def ngg_barabasi_albert(params, out_fn, verbose=True):
    ngg("ngg_barabasi_albert", params, out_fn, verbose=verbose)
def ngg_complete(params, out_fn, verbose=True):
    ngg("ngg_complete", params, out_fn, verbose=verbose)
