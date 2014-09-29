#!/usr/bin/python

import fabric.api
def add():
    fabric.api.local('git add -A')

def commit():
    fabric.api.local('git commit')

def push():
    fabric.api.local('git push')

def prepare_deploy():
    add()
    commit()
    push()
