#! /usr/bin/env python3
'''
FAVITES-Lite
Niema Moshiri 2022
'''

# general imports and load global.json
from os import makedirs, remove
from os.path import abspath, expanduser, isdir, isfile
from shutil import rmtree
from sys import argv, stderr
import json
GLOBAL_JSON_PATH = "%s/global.json" % '/'.join(abspath(expanduser(argv[0])).split('/')[:-1])
GLOBAL = json.loads(open(GLOBAL_JSON_PATH).read())

# FAVITES-Lite-specific imports
from plugins import PLUGIN_FUNCTIONS
from plugins.common import *

# parse user args
def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config', required=True, type=str, help="FAVITES-Lite Config File")
    parser.add_argument('-o', '--output', required=True, type=str, help="Output Directory")
    parser.add_argument('--overwrite', action="store_true", help="Overwrite output directory if it exists")
    parser.add_argument('--version', action="store_true", help="Show FAVITES-Lite version")
    return parser.parse_args()

# validate user args
def validate_args(args, verbose=True):
    if not isfile(args.config):
        error("Config file not found: %s" % args.config)
    if verbose:
        print_log("Config File: %s" % args.config)
    if isdir(args.output) or isfile(args.output):
        if args.overwrite or input('Output directory exists: "%s". Overwrite? (Y/N)' % args.output).upper().startswith('Y'):
            if verbose:
                print_log("Overwriting output directory: %s" % args.output)
            if isdir(args.output):
                rmtree(args.output)
            else:
                remove(args.output)
        else:
            error("Didn't overwrite output directory: %s" % args.output)
    elif verbose:
        print_log("Output Directory: %s" % args.output)

# validate FAVITES-Lite config
def validate_config(config):
    for step in GLOBAL['CONFIG_KEYS']:
        if step not in config:
            error("Invalid config file: Missing step: %s" % step)
        if 'model' not in config[step]:
            error("Invalid config file: Missing model in step: %s" % step)
        model = config[step]['model']
        for p in GLOBAL['MODELS'][step][model]['PARAM']:
            if p not in config[step]['param']:
                error('Invalid config file: Missing parameter for step "%s" model "%s": %s' % (step, model, p))
        if len(config[step]['param']) != len(GLOBAL['MODELS'][step][model]['PARAM']):
            error('Invalid config file: Too many parameters for step "%s" model "%s"' % (step, model))

# run FAVITES-Lite
if __name__ == "__main__":
    print_log("=== FAVITES-Lite v%s ===" % GLOBAL['VERSION'])
    args = parse_args(); validate_args(args)
    config = json.loads(open(args.config).read()); validate_config(config)
    makedirs(args.output); f = open("%s/config.json" % args.output, 'w'); json.dump(config, f); f.close()
    out_fn = {
        'intermediate': "%s/intermediate_files" % args.output,
        'contact_network': "%s/contact_network.tsv" % args.output,
        'transmission_network': "%s/transmission_network.tsv" % args.output,
        'all_state_transitions': "%s/all_state_transitions.tsv" % args.output,
        'sample_times': "%s/sample_times.tsv" % args.output,
        'viral_phylogeny_seeds': "%s/intermediate_files/viral_phylogeny_seed.nwk" % args.output,
        'viral_phylogeny_time': "%s/phylogeny.time.nwk" % args.output,
        'viral_phylogeny_mut': "%s/phylogeny.mutations.nwk" % args.output,
        'sequences': "%s/sequences.fas" % args.output,
    }
    makedirs(out_fn['intermediate']); print_log("Intermediate Files: %s" % out_fn['intermediate'])
    for step in GLOBAL['CONFIG_KEYS']:
        print_log(); print_log("=== %s ===" % step)
        model = config[step]['model'].strip(); print_log("Model: %s" % model)
        params = config[step]['param']
        for p in GLOBAL['MODELS'][step][model]['PARAM']:
            print_log("Parameter: %s: %s" % (p, params[p]))
        if step not in PLUGIN_FUNCTIONS:
            error("Step not implemented yet: %s" % step)
        if model not in PLUGIN_FUNCTIONS[step]:
            error("%s model not implemented yet: %s" % (step, model))
        PLUGIN_FUNCTIONS[step][model](params, out_fn)
