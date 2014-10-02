#!/usr/bin/python

import fabric.api
from configdata import configdict

# create storage account
@fabric.api.task
def createstorageaccount():
    fabric.api.local('azure storage account create %s --label PrimaryStorage --location %s' % (configdict['storageaccountname'], configdict['azurelocation']))

# delete storage account
@fabric.api.task
def deletestorageaccount():
    fabric.api.local('azure storage account delete %s' % configdict['storageaccountname'])

# create virtual machine
@fabric.api.task
def createvm():
    fabric.api.local(r'azure vm create %s b4590d9e3ed742e4a1d46e5424aa335e__openSUSE-13.1-v102 %s --location %s -e -t %s -P' % (configdict['vmname'], configdict['username'], configdict['azurelocation'], configdict['publicsshkeypath']))

# delete virtual machine
@fabric.api.task
def deletevm():
    fabric.api.local('azure vm delete -b -q blrpytest')

# generate private key and a self signed certificate
@fabric.api.task
def createprivatekeyandcert():
    fabric.api.local(r'openssl genrsa -des3 -out %s  2048' % (configdict['privatesshkeypath']))
    fabric.api.local(r'openssl req -new -x509 -key %s -out %s -days %d' % (configdict['privatesshkeypath'], configdict['publicsshcertpath'], 365))
