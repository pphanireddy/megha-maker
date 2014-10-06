#!/usr/bin/python

import os
import fabric.api
from config import configdict

# Add all files except ignored files to git
@fabric.api.task
def add_git():
    fabric.api.local('git add -A')

# Commit added files to git
@fabric.api.task
def commit_git():
    fabric.api.local('git commit')

# Push the committed changes to github
@fabric.api.task
def push_git():
    fabric.api.local('git push')

# Execute the three steps needed to update the latest code
@fabric.api.task
def update_git():
    add_git()
    commit_git()
    push_git()

