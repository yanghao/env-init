import os
from os.path import join as pjoin

from config import HOME, BASE, CONFIG, ENV_URL

def setup_bash():
    fd = open(pjoin(HOME, '.bashrc'), 'a')
    fd.write('\n')
    fd.write("# Generated by env_init\n")
    fd.write("source ~/%s/bashrc\n" % CONFIG)
    fd.close()

def setup_dircolor():
    os.symlink(pjoin(BASE, "dir_colors"), pjoin(HOME, ".dir_colors"))

def setup_vim():
    os.symlink(pjoin(BASE,'vimrc'), pjoin(HOME,'.vimrc')) 
    os.mkdir(pjoin(HOME,".vim"))
    os.symlink(pjoin(BASE, "vim_plugin"), pjoin(HOME, ".vim", "plugin"))
    
def setup_git():
    os.symlink(pjoin(BASE, 'gitconfig'), pjoin(HOME, '.gitconfig'))

def setup_bin():
    os.symlink(pjoin(BASE, 'bin_script'), pjoin(HOME, 'bin'))

def do():
    setup_dircolor()
    setup_bash()
    setup_vim()
    setup_git()
    setup_bin()
