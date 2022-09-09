#! /usr/bin/env python3
from .. import *
from subprocess import call

# simulate a complete graph using ngg_complete
def ngg_complete(params, output_fn, intermediate_path=None, verbose=True):
    command = ['ngg_complete', str(params['n'])]
    if verbose:
        print_log("Command: %s" % ' '.join(command))
    f = open(output_fn, 'w'); call(command, stdout=f); f.close()
