#!/usr/bin/python

import fabric.api
from config import configdict

# create storage account
@fabric.api.task
def create_storageaccount():
    command = (r'azure storage account create %s --label PrimaryStorage --location "%s"' % 
        (configdict['storageaccountname'], configdict['azurelocation']))
    print command
    fabric.api.local(command)

# delete storage account
@fabric.api.task
def delete_storageaccount():
    fabric.api.local(r'azure storage account delete -q %s' % configdict['storageaccountname'])

# create virtual machine
@fabric.api.task
def create_virtualmachine():
    fabric.api.local(r'azure vm create %s %s %s --location "%s" -e -t %s -P' % 
        (configdict['vmname'], configdict['vmimage'], configdict['username'], 
		configdict['azurelocation'], configdict['privatesshpempath']))

# delete virtual machine
@fabric.api.task
def delete_virtualmachine():
    fabric.api.local(r'azure vm delete -b -q %s' % configdict['vmname'])

# add endpoint to vm
@fabric.api.task
def add_vmendpoint(lbport, vmport):
    fabric.api.local(r'azure vm endpoint create %s %s %s' % (configdict['vmname'], lbport, vmport))

# generate private key and a self signed certificate
@fabric.api.task
def create_certificate():
    fabric.api.local(r'openssl genrsa -out %s  2048' % 
		    (configdict['privatesshkeypath']))
    fabric.api.local(r'openssl req -new -x509 -key %s -out %s -days %d' % 
    		    (configdict['privatesshkeypath'], configdict['privatesshpempath'], 365))
