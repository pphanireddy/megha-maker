#!/usr/bin/python

from azure import *
from azure.servicemanagement import *

class NetworkUtil(object):

    # constructor
    def __init__(self, subscription_id, management_pem_path):
        self.sms = ServiceManagementService(subscription_id, management_pem_path)

    # create virtual network
    def create_virtualnetwork(self, servicename, location):
        self.sms.create_hosted_service(servicename, servicename, servicename, location)

    # delete virtual network
    def delete_virtualnetwork(self, servicename):
        self.sms.delete_hosted_service(servicename)

    # create affinity group
    def create_affinity_group(self, name, location):
        self.sms.create_affinity_group(name, name + "_label", location)

    # delete affinity group
    def delete_affinity_group(self, name):
        self.sms.delete_affinity_group(name)

