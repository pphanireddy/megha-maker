#!/usr/bin/python

from azure import *
from azure.servicemanagement import *

class ServiceUtil(object):

    # constructor
    def __init__(self, subscription_id, management_pem_path):
        self.sms = ServiceManagementService(subscription_id, management_pem_path)

    # create cloud service
    def create_cloudservice(self, servicename, location):
        self.sms.create_hosted_service(servicename, servicename, servicename, location)

    # delete cloud service
    def delete_cloudservice(self, servicename):
        self.sms.delete_hosted_service(servicename)
