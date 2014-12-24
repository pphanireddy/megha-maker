#!/usr/bin/python

from azure import *
from azure.servicemanagement import *

class ComputeUtil(object):
    
    # constructor
    def __init__(self, subscription_id, management_pem_path):
        self.sms = ServiceManagementService(subscription_id, management_pem_path)
        self.util = Azureutil(subscription_id, management_pem_path)

    # create linux configuration to be used for creating virtual machine
    def create_vm_conf(self, machinename, username, password, is_ssh_enabled):
        user = username if not None else 'azurecoder'
        passw = passwd if not None else 'Op3nSource'
        confSet = LinuxConfigurationSet(machinename, username, password, is_ssh_enabled)
        confSet.ssh = None
        confSet.disable_ssh_password_authentication = False
        return confSet
 
    # add vm endpoint to the given network configuration
    def add_vm_endpoint(self, networkconf, name, protocol, serviceport, machineport):
        endpoint = ConfigurationSetInputEndpoint(name, protocol, serviceport, machineport)
        networkconf.input_endpoints.input_endpoints.append(endpoint)

    # create vm deployment
    def create_vm_deployment(service, deployment,slot,label,role,vmconf,osvhd,netconf,size):
        result = self.sms.create_virtual_machine_deployment(service,
                        deployment,
                        'production',
                        deployment + 'label',
                        role,
                        vmconf,
                        os_vhd,
                        network_config=network,
                        role_size='Small')
        return result;

    # creates linux vm
    def create_vm_linux(self, service, deployment, location, role, media, hostname, username, passwd):
        vmconf = create_vm_conf(vmname, username, passwd, True)
        os_vhd = OSVirtualHardDisk(source_image_name=Constants.image_name, media_link=media)
        network = ConfigurationSet()
        network.configuration_set_type = 'NetworkConfiguration'
        add_vm_endpoint(network, 'SSH', 'tcp', 22, 22)
        
        # we'll use add role for this. if we have the correct deployment name this should work
        result = self.sms.add_role(service, 
                        deployment, 
                        role, 
                        vmconf, 
                        os_vhd, 
                        network)

        util.wait_for_async(result.request_id)
        util.wait_for_deployment_status(service, deployment, 'Running')
