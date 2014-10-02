#!/usr/bin/python

import fabric.api

# install the required packages to run a tornado app
@fabric.api.task
def installpypackages():
    fabric.api.run('sudo zypper install pip')
    fabric.api.run('sudo pip install fabric')

