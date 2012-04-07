import os
from os.path import join as pjoin
from handle_error import handle
from commands import getstatusoutput as getso

from config import HOME, CONFIG, BASE, ENV_URL

def check_dir():
    import os
    if os.path.exists(BASE):
	return
    else:
        os.mkdir(BASE)
        return

def clone_config():
    s,o = getso("git clone %s %s" % (ENV_URL, BASE))
    handle(s,o)

def do():
    check_dir()
    clone_config()
