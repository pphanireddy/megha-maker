#!/usr/bin/python

import fabric.api

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
def create_virtualmachine(dnsname, vmimage, username, servicename, vmname, location, sshpempath):
    fabric.api.local('azure vm create "%s" "%s" "%s" S@!123 -n "%s" -l "%s" -c "%s" -t "%s" -P -e -v' % 
            (dnsname,
            vmimage,
            username,
            vmname,
	    location,
            servicename,
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
