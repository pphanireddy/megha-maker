#!/usr/bin/python

from azure import *
from azure.servicemanagement import *

class CommonUtil(object):

    # constructor
    def __init__(self, subscription_id, management_pem_path):
        self.sms = ServiceManagementService(subscription_id, management_pem_path)

    # list available locations
    def list_locations(self):
        result = self.sms.list_locations()
        for location in result:
            print(location.name)

    # checks if the image with the given name exists in azure
    def check_image_by_name(self, name): 
        for i in self.sms.list_os_images():
            if name in i.name:
                return True
        return False

    # waits for the async operation to complete
    def wait_for_async_request(self, request_id):
        result = self.sms.get_operation_status(request_id)
        while result.status == 'InProgress':
            sleep(10)
            result = self.sms.get_operation_status(request_id)
        print "successfully completed the request"

    # wait for the deployment to finish
    def wait_for_deployment_status(self, service_name, deployment_name, status):
        props = self.sms.get_deployment_by_name(service_name, deployment_name)
        while props.status != status:
            sleep(10)
            props = self.sms.get_deployment_by_name(service_name, deployment_name)
        print "deployment operation complete - vm is now in " + status + " state"
