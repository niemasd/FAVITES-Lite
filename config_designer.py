#! /usr/bin/env python3
'''
FAVITES-Lite Config Designer
Niema Moshiri 2022
'''

# general imports and load global.json
from datetime import datetime
from glob import glob
from os import getcwd
from os.path import abspath, expanduser, isdir, isfile
from sys import argv, stderr
import json
GLOBAL_JSON_PATH = "%s/global.json" % '/'.join(abspath(expanduser(argv[0])).split('/')[:-1])
GLOBAL = json.loads(open(GLOBAL_JSON_PATH).read())

# return the current time as a string
def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# print to log (prefixed by current time)
def print_log(s='', end='\n'):
    print("[%s] %s" % (get_time(), s), end=end, file=stderr); stderr.flush()

# import prompt_toolkit stuff
try:
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.shortcuts import button_dialog, input_dialog, message_dialog, radiolist_dialog, yes_no_dialog
except:
    print_log("Unable to import prompt_toolkit. Install with: pip install prompt_toolkit"); exit(1)

# welcome page
def page_welcome():
    return button_dialog(
        title="FAVITES-Lite Config Designer v%s" % GLOBAL['VERSION'],
        text="Welcome to the FAVITES-Lite Config Designer!",
        buttons=[
            ('New', page_new_config),
            ('Load', page_load_config),
            ('About', page_about),
            ('Exit', None),
        ]
    ).run()

# about page
def page_about():
    message_dialog(
        title="About",
        text=HTML("<ansired>FAVITES-Lite Config Designer v%s</ansired>\nNiema Moshiri 2022" % GLOBAL['VERSION']),
    ).run()
    return GLOBAL['app']['prev_page']

# new/load config file
def page_newload_config(existing_file):
    tmp = page_find_file(existing_file=existing_file)
    if tmp is None:
        return GLOBAL['app']['prev_page']
    else:
        GLOBAL['app']['config_fn'] = tmp
        return page_dashboard
def page_new_config():
    GLOBAL['config'] = dict()
    return page_newload_config(existing_file=False)
def page_load_config():
    tmp = page_newload_config(existing_file=True)
    GLOBAL['config'] = json.loads(open(GLOBAL['app']['config_fn']).read())
    return tmp

# find a file (either new or existing)
def page_find_file(existing_file):
    # find directory
    curr_dir = "%s/" % abspath(expanduser(getcwd())).rstrip('/')
    while True:
        # create list of directories user can pick 
        vals = [("", "Select current directory: %s" % curr_dir)]
        if curr_dir == '/':
            vals += [('%s/' % d, d[1:]) for d in sorted(glob('/*'))]
        else:
            vals.append(('%s/' % '/'.join(curr_dir.rstrip('/').split('/')[:-1]), '..'))
            vals += [('%s/' % d, d.rstrip('/').split('/')[-1]) for d in sorted(d2 for d2 in glob('%s/*' % curr_dir) if isdir(d2))]
        result = radiolist_dialog(
            title="Select Directory",
            text=None,
            values=vals,
        ).run()

        # user clicked "Cancel"
        if result is None:
            return None

        # if user picks current directory:
        elif result == "":
            if existing_file: # if user is picking an existing file, find it
                while True:
                    vals = [(f.split('/')[-1], f.split('/')[-1]) for f in sorted(f2 for f2 in glob('%s/*' % curr_dir) if isfile(f2) and f2.endswith('.json') and f2 != GLOBAL_JSON_PATH)]
                    fn = radiolist_dialog(
                        title="Select File",
                        text=None,
                        values=vals,
                    ).run()
                    if fn is None: # if user canceled, return to directory selection
                        break
                    else:
                        out = '%s%s' % (curr_dir, fn)
                        if yes_no_dialog(
                            title="Confirm",
                            text="Load the following FAVITES-Lite config file?\n\n%s" % out,
                        ).run():
                            return out
            else:             # if user is creating a new file, ask for file name
                while True:
                    fn = input_dialog(
                        title="Enter Filename",
                        text="Enter filename of new FAVITES-Lite config file:",
                    ).run()
                    if fn is None: # if user canceled, return to directory selection
                        break
                    elif isfile(fn) or isdir(fn):
                        message_dialog(
                            title="Error",
                            text="File exists:\n\n%s" % fn,
                        ).run()
                    elif fn.strip() == "":
                        message_dialog(
                            title="Error",
                            text="File name cannot be empty",
                        ).run()
                    elif not fn.strip().lower().endswith('.json'):
                        message_dialog(
                            title="Error",
                            text="File extension must be .json, but you entered:\n\n%s" % fn,
                        ).run()
                    else:
                        out = '%s%s' % (curr_dir, fn)
                        if yes_no_dialog(
                            title="Confirm",
                            text="Create new FAVITES-Lite config file with the following name?\n\n%s" % out,
                        ).run():
                            return out

        # otherwise move to directory user picked
        else:
            curr_dir = result

# save changes
def page_save():
    f = open(GLOBAL['app']['config_fn'], 'w'); json.dump(GLOBAL['config'], f); f.close()
    message_dialog(
        title="Save",
        text="Changes saved.",
    ).run()
    return GLOBAL['app']['prev_page']

# designer dashboard
def page_dashboard():
    while True:
        tmp = radiolist_dialog(
            title="FAVITES-Lite Config Designer",
            text=HTML("<ansired>Config File:</ansired> %s" % GLOBAL['app']['config_fn']),
            values=[
                (page_save, "Save Changes"),
                (page_about, "About"),
            ],
        ).run()
        if tmp is None and yes_no_dialog(
            title="Exit?",
            text=HTML("Do you want to exit the FAVITES-Lite Config Designer?\n\nNote that this will <b><ansired>*not*</ansired></b> save your changes.\nIf you need to save your changes, click \"No\" and save from the previous page."),
        ).run():
            return None
        elif tmp is not None:
            return tmp

# run the config designer app
if __name__ == "__main__":
    GLOBAL['app'] = {'prev_page':None, 'curr_page':page_welcome}
    while GLOBAL['app']['curr_page'] is not None:
        GLOBAL['app']['curr_page'], GLOBAL['app']['prev_page'] = GLOBAL['app']['curr_page'](), GLOBAL['app']['curr_page']
