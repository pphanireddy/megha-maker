#!/usr/bin/python

import os
import fabric.api
import azureoperations
import deployoperations
from configdata import configdict

# Add all files except ignored files to git
@fabric.api.task
def add():
    fabric.api.local('git add -A')

# Commit added files to git
@fabric.api.task
def commit():
    fabric.api.local('git commit')

# Push the committed changes to github
@fabric.api.task
def push():
    fabric.api.local('git push')

# Execute the three steps needed to update the latest code
@fabric.api.task
def prepare_deploy():
    add()
    commit()
    push()

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

#Simple command to test
@fabric.api.task
def uname():
    fabric.api.run ('uname -a')

