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
STEP_TO_IND = {k:i for i,k in enumerate(GLOBAL['CONFIG_KEYS'])}

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

# save config file
def save_config():
    f = open(GLOBAL['app']['config_fn'], 'w'); json.dump(GLOBAL['config'], f); f.close()

# parse parameter value
def parse_param_value(value, param_type):
    try:
        if param_type == "integer":
            return int(value)
        elif param_type == "positive integer":
            value = int(value)
            if value > 0:
                return value
        elif param_type == "even positive integer":
            value = int(value)
            if value > 0 and value % 2 == 0:
                return value
        elif param_type == "non-negative integer":
            value = int(value)
            if value >= 0:
                return value
        elif param_type == "float":
            return float(value)
        elif param_type == "positive float":
            value = float(value)
            if value > 0:
                return value
        elif param_type == "non-negative float":
            value = float(value)
            if value >= 0:
                return value
        elif param_type == "probability":
            value = float(value)
            if 0 <= value <= 1:
                return value
        else:
            print_log("FAVITES-Lite bug: Invalid parameter type: %s" % param_type); exit(1)
    except:
        return None

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
        text=HTML("<ansigreen>FAVITES-Lite Config Designer v%s</ansigreen> - <ansired>Niema Moshiri 2022</ansired>" % GLOBAL['VERSION']),
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
    if 'config_fn' in GLOBAL['app']:
        GLOBAL['config'] = json.loads(open(GLOBAL['app']['config_fn']).read())
    return tmp

# find a file (either new or existing)
def page_find_file(existing_file):
    # find directory
    curr_dir = "%s/" % abspath(expanduser(getcwd())).rstrip('/')
    while True:
        # create list of directories user can pick 
        vals = [("", HTML("<ansigreen>Select current directory: %s</ansigreen>" % curr_dir))]
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
                            text=HTML("Load the following FAVITES-Lite config file?\n\n<ansigreen>%s</ansigreen>" % out),
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
                            text=HTML("File exists:\n\n<ansired>%s</ansired>\n\nOverwrite?" % fn),
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
                            text=HTML("Create new FAVITES-Lite config file with the following name?\n\n<ansigreen>%s</ansigreen>" % out),
                        ).run():
                            return out

        # otherwise move to directory user picked
        else:
            curr_dir = result

# save changes
def page_save():
    save_config()
    message_dialog(
        title="Save",
        text="FAVITES-Lite config file saved:\n\n%s" % GLOBAL['app']['config_fn'],
    ).run()
    return GLOBAL['app']['prev_page']

# all steps (e.g. Contact Network, Transmission Network), etc. will use the same infrastructure to pick model
STEP_TO_PAGE = {k: (lambda k=k: page_model_selection(k)) for k in GLOBAL['CONFIG_KEYS']}
def page_model_selection(step):
    while True:
        # pick model
        model = radiolist_dialog(
            title=step,
            text=HTML("<ansigreen>Description:</ansigreen>\n%s\n\n<ansigreen>Models:</ansigreen>" % GLOBAL['DESC'][step]),
            values=[(m, m) for m in GLOBAL['MODELS'][step]]
        ).run()
        if model is None:
            return GLOBAL['app']['prev_page']
        text = "Do you want to select the <ansired>%s</ansired> model?" % model
        if 'DESC' in GLOBAL['MODELS'][step][model]:
            text += ("\n\n<ansigreen>Description:</ansigreen>\n%s" % GLOBAL['MODELS'][step][model]['DESC'])
        if 'PROP' in GLOBAL['MODELS'][step][model] and len(GLOBAL['MODELS'][step][model]['PROP']) != 0:
            text += ("\n\n<ansigreen>Properties:</ansigreen>\n%s" % '\n'.join(("  - %s" % p) for p in GLOBAL['MODELS'][step][model]['PROP']))
        if yes_no_dialog(
            title=step,
            text=HTML(text),
        ).run():
            GLOBAL['config'][step] = {'model':model, 'param':dict()}
            return lambda step=step: page_view_params(i=STEP_TO_IND[step], show_nav=False)

# page to set a specific model parameter
def page_parameter_selection(step, model, p):
    while True:
        text = "Please enter value for <ansired>%s</ansired> model parameter: <ansired>%s</ansired>\n\n<ansigreen>Type:</ansigreen> %s" % (model, p, GLOBAL['MODELS'][step][model]['PARAM'][p]['TYPE'])
        if 'DESC' in GLOBAL['MODELS'][step][model]['PARAM'][p]:
            text += "\n\n<ansigreen>Description:</ansigreen> %s" % GLOBAL['MODELS'][step][model]['PARAM'][p]['DESC']
        v = input_dialog(
            title=step,
            text=HTML(text)
        ).run()
        if v is None:
            return GLOBAL['app']['prev_page']
        v = v.strip()
        if len(v) == 0:
            message_dialog(
                title="Error",
                text="You did not enter anything",
            ).run()
            continue
        v_parse = parse_param_value(v, GLOBAL['MODELS'][step][model]['PARAM'][p]['TYPE'])
        if v_parse is None:
            message_dialog(
                title="Error",
                text=HTML("<ansired>%s</ansired> model parameter <ansired>%s</ansired> must be: %s\n\nYou entered: %s" % (model, p, GLOBAL['MODELS'][step][model]['PARAM'][p]['TYPE'], v)),
            ).run()
        else:
            GLOBAL['config'][step]['param'][p] = v_parse
            return GLOBAL['app']['prev_page']

# view parameter selection from dashboard
def page_view_params(i=0, show_nav=True):
    while True:
        step = GLOBAL['CONFIG_KEYS'][i]
        if step in GLOBAL['config'] and GLOBAL['config'][step] is not None and 'model' in GLOBAL['config'][step]:
            model = GLOBAL['config'][step]['model']
        else:
            model = None
        tmp = {True:'ansired',False:'ansigreen'}[model is None]
        text = "Model: <%s>%s</%s>" % (tmp, {True:"Not selected",False:model}[model is None], tmp)
        vals = list()
        if show_nav:
            title = "%s (%d/%d)" % (step, i+1, len(GLOBAL['CONFIG_KEYS']))
            if i != len(GLOBAL['CONFIG_KEYS'])-1:
                vals.append(('next', HTML('<ansimagenta>Next Step (%s)</ansimagenta>' % GLOBAL['CONFIG_KEYS'][i+1])))
            if i != 0:
                vals.append(('prev', HTML('<ansimagenta>Previous Step (%s)</ansimagenta>' % GLOBAL['CONFIG_KEYS'][i-1])))
        else:
            title = step
            if model is not None and len(GLOBAL['MODELS'][step][model]['PARAM']) != 0:
                text += "\n\nParameters:"
        if model is not None:
            for p in GLOBAL['MODELS'][step][model]['PARAM']:
                if p in GLOBAL['config'][step]['param']:
                    p_val = GLOBAL['config'][step]['param'][p]
                else:
                    p_val = None
                tmp = {True:'ansired',False:'ansigreen'}[p_val is None]
                p_text = "<%s>%s</%s>: " % (tmp, p, tmp)
                if 'DESC' in GLOBAL['MODELS'][step][model]['PARAM'][p]:
                    p_text += "%s: " % GLOBAL['MODELS'][step][model]['PARAM'][p]['DESC']
                p_text += "<%s>%s</%s>" % (tmp, {True:"Not selected",False:p_val}[p_val is None], tmp)
                vals.append((lambda step=step, model=model, p=p: page_parameter_selection(step,model,p), HTML(p_text)))
        if len(vals) == 0:
            return page_dashboard
        tmp = radiolist_dialog(
            title=title,
            text=HTML(text),
            values=vals,
            cancel_text="Return",
        ).run()
        if tmp is None:
            return page_dashboard
        elif tmp == 'prev':
            i -= 1
        elif tmp == 'next':
            i += 1
        else:
            return tmp

# designer dashboard
def page_dashboard():
    while True:
        # set dashboard text
        complete = True
        for k in GLOBAL['CONFIG_KEYS']:
            if k not in GLOBAL['config'] or GLOBAL['config'][k] is None or len(GLOBAL['config'][k]['param']) != len(GLOBAL['MODELS'][k][GLOBAL['config'][k]['model']]['PARAM']):
                complete = False; break
        tmp = {True:"ansigreen", False:"ansired"}[complete]
        text = "<%s>Config File:</%s> %s" % (tmp, tmp, GLOBAL['app']['config_fn'])
        vals = list()
        for k in GLOBAL['CONFIG_KEYS']:
            if k in GLOBAL['config'] and GLOBAL['config'][k] is not None:
                tmp = {True:"ansigreen", False:"ansired"}[len(GLOBAL['config'][k]['param']) == len(GLOBAL['MODELS'][k][GLOBAL['config'][k]['model']]['PARAM'])]
                m = "<%s>%s</%s>" % (tmp, GLOBAL['config'][k]['model'], tmp)
            else:
                m = "<ansired>Not selected</ansired>"
            vals.append((STEP_TO_PAGE[k], HTML("%s: %s" % (k,m))))
        vals += [
            (page_view_params, "View/Edit Parameters"),
            (page_save, "Save Changes"),
            (page_about, "About"),
        ]

        # run dashboard
        tmp = radiolist_dialog(
            title="FAVITES-Lite Config Designer",
            text=HTML(text),
            cancel_text="Exit",
            values=vals,
        ).run()
        if tmp is None:
            tmp = button_dialog(
                title="Exit?",
                text=HTML("Do you want to exit the FAVITES-Lite Config Designer?\n  - <ansired>Yes (Save)</ansired> = Exit and save changes\n  - <ansired>Yes (Disc)</ansired> = Exit and discard changes\n  - <ansired>No</ansired> = Don't exit"),
                buttons=[
                    ("Yes (Save)", 'save'),
                    ("Yes (Disc)", None),
                    ("No", page_dashboard),
                ],
            ).run()
            if tmp == 'save':
                save_config()
                return None
            else:
                return tmp
        else:
            return tmp

# run the config designer app
if __name__ == "__main__":
    GLOBAL['app'] = {'prev_page':None, 'curr_page':page_welcome}
    while GLOBAL['app']['curr_page'] is not None:
        GLOBAL['app']['curr_page'], GLOBAL['app']['prev_page'] = GLOBAL['app']['curr_page'](), GLOBAL['app']['curr_page']
