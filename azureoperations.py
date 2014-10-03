#!/usr/bin/python

import fabric.api
from configdata import configdict

# create storage account
@fabric.api.task
def createstorageaccount():
    fabric.api.local(r'azure storage account create %s --label PrimaryStorage --location "%s"' % 
        (configdict['storageaccountname'], configdict['azurelocation']))

# delete storage account
@fabric.api.task
def deletestorageaccount():
    fabric.api.local(r'azure storage account delete -q %s' % configdict['storageaccountname'])

# create virtual machine
@fabric.api.task
def createvm():
    fabric.api.local(r'azure vm create %s %s %s --location "%s" -e -t %s -P' % 
        (configdict['vmname'], configdict['vmimage'], configdict['username'], 
		configdict['azurelocation'], configdict['publicsshcertpath']))

# delete virtual machine
@fabric.api.task
def deletevm():
    fabric.api.local(r'azure vm delete -b -q %s' % configdict['vmname'])

# generate private key and a self signed certificate
@fabric.api.task
def createprivatekeyandcert():
    fabric.api.local(r'openssl genrsa -des3 -out %s  2048' % 
		    (configdict['privatesshkeypath']))
    fabric.api.local(r'openssl req -new -x509 -key %s -out %s -days %d' % 
		    (configdict['privatesshkeypath'], configdict['publicsshcertpath'], 365))
