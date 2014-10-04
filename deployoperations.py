#!/usr/bin/python

import fabric.api

# install the required packages to run a tornado app
@fabric.api.task
def installpypackages():
    fabric.api.run('sudo apt-get install -y python-pip python-dev build-essential')
    fabric.api.run('sudo pip install --upgrade pip')
    fabric.api.run('sudo pip install --upgrade virtualenv')
    fabric.api.run('sudo pip install --upgrade tornado')
    fabric.api.run('sudo apt-get install -y fabric')
    fabric.api.run('sudo apt-get install -y git')

#clone the required repository and start the app
@fabric.api.task
def cloneandstartapp():
    fabric.api.run(r'rm -rf azure-tornado-app')
    fabric.api.run(r'git clone https://github.com/pphanireddy/azure-tornado-app.git')
    fabric.api.run(r'python azure-tornado-app/tornadoapp/HelloWorld.py')    
