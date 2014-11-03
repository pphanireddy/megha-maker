#!/usr/bin/python

import os
import fabric.api
import azure
import service

# create virtual machines for the role
def create_role(path, serviceobject, roleobject, sshstartport):
    for i in range(0, roleobject.machine.count):
        azure.create_virtualmachine(serviceobject.name,
                roleobject.machine.image,
                roleobject.name,
                ( '%s_%d' % (roleobject.name, i)),
                roleobject.machine.location,
                os.path.join(path, roleobject.security.sshpempath),
                sshstartport + i)

# delete virtual machines for the role
def delete_role(path, serviceobject, roleobject):
    for i in range(0, roleobject.machine.count):
        azure.delete_virtualmachine(( '%s_%d' % (roleobject.name, i)))

# creates the specified service
@fabric.api.task
def create_service(path):
    servicexmldoc = file(os.path.join(path, 'service.xml')).read()
    serviceobject = service.CreateFromDocument(servicexmldoc)
    azure.create_cloudservice(serviceobject.name, serviceobject.location)
    azure.create_storageaccount(serviceobject.name, serviceobject.location)

    sshstartport = 22
    for roleobject in serviceobject.role:
        create_role(path, serviceobject, roleobject, sshstartport)
        sshstartport = sshstartport + 10

# deletes the specified service
@fabric.api.task
def delete_service(path):
    servicexmldoc = file(os.path.join(path, 'service.xml')).read()
    serviceobject = service.CreateFromDocument(servicexmldoc)

    for roleobject in serviceobject.role:
        delete_role(path, serviceobject, roleobject)

    azure.delete_storageaccount(serviceobject.name)
    azure.delete_cloudservice(serviceobject.name)
