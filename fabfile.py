#!/usr/bin/python

import fabric.api

# Add all files except ignored files to git
def add():
    fabric.api.local('git add -A')

# Commit added files to git
def commit():
    fabric.api.local('git commit')

# Push the committed changes to github
def push():
    fabric.api.local('git push')

# Execute the three steps needed to update the latest code
def prepare_deploy():
    add()
    commit()
    push()

# Set the hosts for a command
def set_hosts(filename):
    fabric.api.env.hosts = open(filename, 'r').read().splitlines()

# Set private keys used for ssh
def set_keys(filename):
    fabric.api.env.key_filename = open(filename, 'r').read().splitlines()

#Simple command to test
def uname():
    fabric.api.run ('uname -a')

