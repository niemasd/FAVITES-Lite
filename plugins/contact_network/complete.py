#! /usr/bin/env python3
from .. import *
from subprocess import call

# simulate a complete graph using ngg_complete
def ngg_complete(params, out_fn, verbose=True):
    command = ['ngg_complete', str(params['n'])]
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    f = open(out_fn['contact_network'], 'w'); call(command, stdout=f); f.close()
    if verbose:
        print_log("Contact Network written to: %s" % out_fn['contact_network'])
