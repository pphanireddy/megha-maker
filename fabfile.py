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
