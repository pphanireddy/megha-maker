#!/usr/bin/python

import fabric.api

def commit():
    fabric.api.local('git add -p && git commit')

def push():
    fabric.api.local('git push')

def prepare_deploy():
    commit()
    push()
