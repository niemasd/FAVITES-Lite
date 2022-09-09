#! /usr/bin/env python3
'''
FAVITES-Lite
Niema Moshiri 2022
'''

# general imports and load global.json
from os import remove
from os.path import abspath, expanduser, isdir, isfile
from shutil import rmtree
from sys import argv, stderr
import json
GLOBAL_JSON_PATH = "%s/global.json" % '/'.join(abspath(expanduser(argv[0])).split('/')[:-1])
GLOBAL = json.loads(open(GLOBAL_JSON_PATH).read())

# FAVITES-Lite-specific imports
from plugins.common import *

# parse user args
def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-c', '--config', required=True, type=str, help="FAVITES-Lite Config File")
    parser.add_argument('-o', '--output', required=True, type=str, help="Output Directory")
    parser.add_argument('--overwrite', action="store_true", help="Overwrite output directory if it exists")
    parser.add_argument('--version', action="store_true", help="Show FAVITES-Lite version")
    args = parser.parse_args()
    if not isfile(args.config):
        error("Config file not found: %s" % args.config)
    print_log("Config File: %s" % args.config)
    if isdir(args.output) or isfile(args.output):
        if args.overwrite or input('Output directory exists: "%s". Overwrite? (Y/N)' % args.output).upper().startswith('Y'):
            print_log("Overwriting output directory: %s" % args.output)
            if isdir(args.output):
                rmtree(args.output)
            else:
                remove(args.output)
        else:
            error("Didn't overwrite output directory: %s" % args.output)
    else:
        print_log("Output Directory: %s" % args.output)
    return args

# run FAVITES-Lite
if __name__ == "__main__":
    print_log("=== FAVITES-Lite v%s ===" % GLOBAL['VERSION'])
    args = parse_args()
