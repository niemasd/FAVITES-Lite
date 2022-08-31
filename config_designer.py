#! /usr/bin/env python3
'''
FAVITES-Lite Config Designer
Niema Moshiri 2022
'''

# general imports and load global.json
from datetime import datetime
from json import loads as jloads
from os.path import abspath, expanduser
from sys import argv, stderr
GLOBAL = jloads(open("%s/global.json" % '/'.join(abspath(expanduser(argv[0])).split('/')[:-1])).read())

# return the current time as a string
def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# print to log (prefixed by current time)
def print_log(s='', end='\n'):
    print("[%s] %s" % (get_time(), s), end=end, file=stderr); stderr.flush()

# import prompt_toolkit stuff
try:
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.shortcuts import button_dialog, message_dialog
except:
    print_log("Unable to import prompt_toolkit. Install with: pip install prompt_toolkit"); exit(1)

# welcome page
def page_welcome():
    return button_dialog(
        title="FAVITES-Lite v%s" % GLOBAL['VERSION'],
        text="Welcome to FAVITES-Lite!",
        buttons=[
            ('New', None), # TODO
            ('Load', None), # TODO
            ('About', page_about),
            ('Exit', None),
        ]
    ).run()

# about page
def page_about():
    message_dialog(
        title="About",
        text=HTML("<ansired>FAVITES-Lite v%s</ansired>\nNiema Moshiri 2022" % GLOBAL['VERSION']),
    ).run()
    return GLOBAL['app']['prev_page']

# main content
if __name__ == "__main__":
    GLOBAL['app'] = {'prev_page':None, 'curr_page':page_welcome}
    while GLOBAL['app']['curr_page'] is not None:
        GLOBAL['app']['curr_page'], GLOBAL['app']['prev_page'] = GLOBAL['app']['curr_page'](), GLOBAL['app']['curr_page']
