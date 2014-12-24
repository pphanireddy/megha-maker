#!/usr/bin/python

import fabric.api
from commonutil import *
from computeutil import *
from storageutil import *
from serviceutil import *

# List azure locations
@fabric.api.task
def get_azure_locations():
    manager=CommonUtil(r'3fec5be7-3873-45ca-b19d-fc0f879be4c0', 
            r'/home/blr/cloudinfra/secretstorage/azure.pem')
    manager.list_locations()

@fabric.api.task
deb create_application():

