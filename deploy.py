#!/usr/bin/python

import os
import fabric.api
from config import configdict

# installs the standard packages required by the service
@fabric.api.task
def install_packages():
    fabric.api.local('git add -A')

# installs hadoop
@fabric.api.task
def install_hadoop():
    fabric.api.local('git commit')
