import os
from os.path import join as pjoin
from handle_error import handle
from commands import getstatusoutput as getso

HOME = os.environ['HOME']
CONFIG = 'env_config'
BASE = pjoin(HOME, CONFIG)

def check_dir():
    import os
    if os.path.exists(BASE):
	return
    else:
        os.mkdir(BASE)
        return

def clone_config():
    s,o = getso("git clone ssh://xiytw007/home/hua/git_dev/config ~/env_config")
    handle(s,o)

def do():
    check_dir()
    clone_config()
