#!/usr/bin/python

import fabric.api

# install the required packages to run a tornado app
@fabric.api.task
def installpypackages():
    fabric.api.run('sudo su -')
    fabric.api.run('zypper install pip')
    fabric.api.run('pip install fabric')

