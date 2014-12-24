#!/usr/bin/python

from azure import *
from azure.servicemanagement import *

class StorageUtil(object):

    # constructor
    def __init__(self, subscription_id, management_pem_path):
        self.sms = ServiceManagementService(subscription_id, management_pem_path)

    # create storage account
    def create_storageaccount(self, storagename, location):
        self.sms.create_storage_account (storagename, storagename, storagename, location)

    # delete storage account
    def delete_storageaccount(self, storagename):
        self.sms.delete_storage_account(storagename)

