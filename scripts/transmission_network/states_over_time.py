#! /usr/bin/env python3
'''
Plot the number of individuals in each state of the transmission network over time
'''
from os.path import isdir, isfile
from sys import stderr
import argparse
try:
    from seaborn import lineplot, set_context, set_style
except:
    stderr.write("ERROR: Unable to import seaborn. Install with: pip install seaborn\n"); exit(1)
try:
    import matplotlib
    import matplotlib.pyplot as plt
except:
    stderr.write("ERROR: Unable to import matplotlib. Install with: pip install matplotlib\n"); exit(1)
RC = {"font.size":12,"axes.titlesize":16,"axes.labelsize":14,"legend.fontsize":10,"xtick.labelsize":10,"ytick.labelsize":10}
set_context("paper", rc=RC); set_style("ticks"); matplotlib.rcParams['font.family'] = 'serif'
matplotlib.use('Agg')

# main content
if __name__ == "__main__":
    # parse user args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=True, type=str, help="Input 'All State Transitions' File")
    parser.add_argument('-o', '--output', required=True, type=str, help="Output File (PDF)")
    parser.add_argument('-t', '--title', required=False, type=str, default="States Over Time", help="Figure Title")
    parser.add_argument('-xl', '--xlabel', required=False, type=str, default="Time", help="X-Axis Label")
    parser.add_argument('-yl', '--ylabel', required=False, type=str, default="Number of Individuals", help="Y-Axis Label")
    parser.add_argument('-xm', '--xmin', required=False, type=float, default=0, help="X-Axis Minimum")
    parser.add_argument('-xM', '--xmax', required=False, type=float, default=None, help="X-Axis Maximum")
    parser.add_argument('-ym', '--ymin', required=False, type=float, default=0, help="Y-Axis Minimum")
    parser.add_argument('-yM', '--ymax', required=False, type=float, default=None, help="Y-Axis Maximum")
    parser.add_argument('--hide_legend', action="store_true", help="Hide figure legend")
    parser.add_argument('--overwrite', action="store_true", help="Overwrite output file if it exists")
    args = parser.parse_args()

    # check args
    if not isfile(args.input):
        print("ERROR: Input file not found: %s" % args.input, file=stderr); exit(1)
    if (not args.overwrite) and (isfile(args.output) or isdir(args.output)):
        print("ERROR: Output file exists: %s" % args.output, file=stderr); exit(1)
    elif not args.output.lower().endswith('.pdf'):
        print("ERROR: Output file extension must be PDF", file=stderr); exit(1)
    args.title = args.title.strip(); args.xlabel = args.xlabel.strip(); args.ylabel = args.ylabel.strip()

    # load data from input file
    count = dict() # count[state] = number of individuals in that state
    data_x = list(); data_y = list(); data_s = list() # store times (x), counts (y), and state labels (s)
    for l in open(args.input):
        node, from_s, to_s, t = [v.strip() for v in l.split('\t')]; t = float(t)
        if from_s != 'None':
            count[from_s] -= 1; data_x.append(t); data_y.append(count[from_s]); data_s.append(from_s)
        if to_s not in count:
            count[to_s] = 0
        count[to_s] += 1; data_x.append(t); data_y.append(count[to_s]); data_s.append(to_s)
    for s in count:
        data_x.append(t); data_y.append(count[s]); data_s.append(s)
    if args.xmax is None:
        args.xmax = t

    # create plot
    fig = plt.figure()
    lineplot(x=data_x, y=data_y, hue=data_s)
    plt.xlim(args.xmin, args.xmax)
    plt.ylim(args.ymin, args.ymax)
    if len(args.title) != 0:
        plt.title(args.title)
    if len(args.xlabel) != 0:
        plt.xlabel(args.xlabel)
    if len(args.ylabel) != 0:
        plt.ylabel(args.ylabel)
    if args.hide_legend:
        plt.legend([],[], frameon=False)
    fig.savefig(args.output, format='pdf', bbox_inches='tight')
