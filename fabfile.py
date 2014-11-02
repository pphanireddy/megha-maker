#!/usr/bin/python

import os
import fabric.api
import barista

# Set the hosts for a command
@fabric.api.task
def set_hosts(filename):
    fabric.api.env.user = 'blr'
    fabric.api.env.hosts = open(filename, 'r').read().splitlines()

# Set private keys used for ssh
@fabric.api.task
def set_keys():
    fabric.api.env.key_filename = configdict['privatesshkeypath']
    print fabric.api.env.key_filename

# Simple command to test
@fabric.api.task
def get_uname():
    fabric.api.run ('uname -a')

