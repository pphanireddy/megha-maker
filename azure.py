#!/usr/bin/python

import fabric.api
from config import configdict

# create cloud service
def create_cloudservice(servicename, location):
    fabric.api.local(r'azure service create --serviceName %s --location "%s"' %
            (servicename, 
            location))

# delete cloud service
def delete_cloudservice(servicename):
    fabric.api.local(r'azure service delete --quiet --serviceName %s' %
            servicename)
        
# create storage account
def create_storageaccount(storageaccountname, location):
    fabric.api.local(r'azure storage account create %s --label PrimaryStorage --location "%s"' % 
            (storageaccountname, 
            location))

# delete storage account
def delete_storageaccount(storageaccountname):
    fabric.api.local(r'azure storage account delete -q %s' % 
            storageaccountname)

# create virtual machine
def create_virtualmachine(vmname, vmimage, username, location, sshpempath):
    fabric.api.local(r'azure vm create %s %s %s --location "%s" -e -t %s -P' % 
            (vmname, 
            vmimage, 
            username, 
	    location, 
            sshpempath))

# delete virtual machine
def delete_virtualmachine(vmname):
    fabric.api.local(r'azure vm delete -b -q %s' % 
            vmname)

# add endpoint to vm
def add_vmendpoint(vmname, lbport, vmport):
    fabric.api.local(r'azure vm endpoint create %s %s %s' % 
            (vmname, 
            lbport, 
            vmport))

# generate private key and a self signed certificate
@fabric.api.task
def create_certificate():
    fabric.api.local(r'openssl genrsa -out %s  2048' % 
	    (configdict['privatesshkeypath']))
    fabric.api.local(r'openssl req -new -x509 -key %s -out %s -days %d' % 
    	    (configdict['privatesshkeypath'], 
            configdict['privatesshpempath'], 
            365))
