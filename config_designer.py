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
    GLOBAL['config'] = {"Contact Network":None}
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
                        if yes_no_dialog(
                            title="File Exists",
                            text="File exists:\n\n%s\n\nOverwrite?" % fn,
                        ).run():
                            return '%s%s' % (curr_dir, fn)
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
        text="FAVITES-Lite config file saved:\n\n%s" % GLOBAL['app']['config_fn'],
    ).run()
    return GLOBAL['app']['prev_page']

# contact network configuration
def page_contact_network():
    # pick model
    model = None
    while True:
        model = radiolist_dialog(
            title="Contact Network: Model",
            text=None,
            values=[(m, m) for m in GLOBAL['MODELS']['Contact Network']]
        ).run()
        if model is None:
            return GLOBAL['app']['prev_page']
        text = "Do you want to select the <ansired>%s</ansired> model?" % model
        if 'DESC' in GLOBAL['MODELS']['Contact Network'][model]:
            text += ("\n\n%s" % GLOBAL['MODELS']['Contact Network'][model]['DESC'])
        if 'PARAM' in GLOBAL['MODELS']['Contact Network'][model] and len(GLOBAL['MODELS']['Contact Network'][model]['PARAM']) != 0:
            text += "\n\n<ansigreen>Parameters:</ansigreen>"
            for p in GLOBAL['MODELS']['Contact Network'][model]['PARAM']:
                text += ("\n  - <ansired>%s</ansired>" % p)
                if 'DESC' in GLOBAL['MODELS']['Contact Network'][model]['PARAM'][p]:
                    text += (': %s' % GLOBAL['MODELS']['Contact Network'][model]['PARAM'][p]['DESC'])
        if 'PROP' in GLOBAL['MODELS']['Contact Network'][model] and len(GLOBAL['MODELS']['Contact Network'][model]['PROP']) != 0:
            text += ("\n\n<ansigreen>Properties:</ansigreen>\n%s" % '\n'.join(("  - %s" % p) for p in GLOBAL['MODELS']['Contact Network'][model]['PROP']))
        if yes_no_dialog(
            title=model,
            text=HTML(text),
        ).run():
            break

    # set model parameters
    print(model); exit(1) # TODO
    return page_dashboard

# designer dashboard
def page_dashboard():
    while True:
        # set dashboard text
        complete = True
        for k in GLOBAL['CONFIG_KEYS']:
            if k not in GLOBAL['config'] or GLOBAL['config'][k] is None:
                complete = False; break
        tmp = {True:"ansigreen", False:"ansired"}[complete]
        text = "<%s>Config File:</%s> %s" % (tmp, tmp, GLOBAL['app']['config_fn'])
        for k in GLOBAL['CONFIG_KEYS']:
            tmp = {True:"ansigreen", False:"ansired"}[k in GLOBAL['config'] and GLOBAL['config'][k] is not None]
            text += "\n  - <%s>Contact Network:</%s> %s" % (tmp, tmp, GLOBAL['config'][k])

        # run dashboard
        tmp = radiolist_dialog(
            title="FAVITES-Lite Config Designer",
            text=HTML(text),
            values=[
                (page_contact_network, "Contact Network"),
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
