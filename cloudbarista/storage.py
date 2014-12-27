#!/usr/bin/python

from azure import *
from azure.servicemanagement import *
from utility import *

class Storage(object):

    # constructor
    def __init__(self, subscription_id, management_pem_path):
        self.sms = ServiceManagementService(subscription_id, management_pem_path)
        self.util = Utility(subscription_id, management_pem_path)

    # create storage account
    def create_storageaccount(self, name, location, issync):
        result  = self.sms.create_storage_account(name, name, name, location=location)
        if issync:
            self.util.wait_for_async_request(result.request_id)

    # delete storage account
    def delete_storageaccount(self, storagename, issync):
        self.sms.delete_storage_account(storagename)

