#!/usr/bin/python

from azure import *
from azure.servicemanagement import *
from utility import *

class Compute(object):
    
    # constructor
    def __init__(self, subscription_id, management_pem_path):
        self.sms = ServiceManagementService(subscription_id, management_pem_path)
        self.util = Utility(subscription_id, management_pem_path)

    # create linux configuration to be used for creating virtual machine
    def create_vm_conf(self, machinename, username, password, disable_ssh_passwd_auth):
        confSet = LinuxConfigurationSet(machinename, username, password, disable_ssh_passwd_auth)
        confSet.ssh = None
        return confSet
 
    # add vm endpoint to the given network configuration
    def add_vm_endpoint(self, networkconf, name, protocol, serviceport, machineport):
        endpoint = ConfigurationSetInputEndpoint(name, protocol, serviceport, machineport)
        networkconf.input_endpoints.input_endpoints.append(endpoint)
        return networkconf

    # create vm deployment
    def create_vm_deployment(self, service, deployId, slot, roleId, vmconf, osvhd, netconf, size):
        result = self.sms.create_virtual_machine_deployment(service,
                        str(deployId),
                        slot,
                        str(roleId),
                        roleId,
                        vmconf,
                        osvhd,
                        network_config=netconf,
                        role_size=size)
        return result

    # append vm deployment
    def append_vm_deployment(self, service, deployId, roleId, vmconf, osvhd, netconf, size):
        result = self.sms.add_role(service,
                        str(deployId),
                        roleId,
                        vmconf,
                        osvhd,
                        network_config=netconf,
                        role_size=size)
        return result
