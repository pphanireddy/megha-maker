#!/usr/bin/python

import os
import uuid
from compute import *
from storage import *
from service import *
import topology
import traceback
import random

class Barista(object):

    def __init__(self, subscription_id, management_pem_path, topology_xml_path):
        '''
        Constructor

        subscription_id:
            The azure subscription id
        management_pem_path:
            The path to the azure management certificate pem file
        topology_xml_path:
            The path to the xml file that contains the configs for the application
        '''

        self.service = Service(subscription_id, management_pem_path)
        self.storage = Storage(subscription_id, management_pem_path)
        self.compute = Compute(subscription_id, management_pem_path)
        self.utility = Utility(subscription_id, management_pem_path)
        xmldoc = file(os.path.join(topology_xml_path)).read()
        self.topology = topology.CreateFromDocument(xmldoc)

    def create_application(self):
        '''
        Creates the application
        '''

        try:
            service_conf = self.topology.service
            storage_conf = self.topology.storage
            compute_conf = self.topology.compute

            self.service.create_cloudservice(service_conf.name, service_conf.region)
            #self.storage.create_storageaccount(storage_conf.name, service_conf.region, True)
            for role_conf in compute_conf.role:
                    self.create_role(role_conf, service_conf, storage_conf)

        except Exception as e:
                print('AZURE ERROR: %s' % str(e))
                print(traceback.format_exc())
                return False

    def delete_application(self):
        '''
        Deletes the application
        '''

        try:
            service_conf = self.topology.service
            storage_conf = self.topology.storage
            compute_conf = self.topology.compute

            for role_conf in compute_conf.role:
                    self.delete_role(role_conf)

            self.service.delete_cloudservice(service_conf.name)
            self.storage.delete_account(storage_conf.name)

        except Exception as e:
                print('AZURE ERROR: %s' % str(e))
                print(traceback.format_exc())
                return False

    def create_role(self, role_conf, service_conf, storage_conf):
        '''
        Creates the role
        '''
        try:
            deploymentId = uuid.uuid1()
            print('Creating deployment: ' + str(deploymentId))
            for i in range(0, role_conf.count):
                result = None
                vmconf = self.compute.create_vm_conf(role_conf.id + '_' + str(i), 
                                    role_conf.vmconf.ssh.username, 
                                    role_conf.vmconf.ssh.password, 
                                    role_conf.vmconf.ssh.disablepasswordauth)
                
                netconf = ConfigurationSet()
                netconf.configuration_set_type = 'NetworkConfiguration'
                for endpoint in role_conf.netconf.endpoint:
                    servicePort = None
                    if endpoint.isloadbalanced == 'True':
                        servicePort = int(endpoint.cloud) 
                    else:
                        servicePort = int(endpoint.start) + i
                        
                    netconf = self.compute.add_vm_endpoint(netconf,
                                    endpoint.name + str(i), 
                                    endpoint.protocol, 
                                    servicePort,
                                    endpoint.local)
                
                media_link = "http://" + role_conf.osvhd.media.storageid + ".blob.core.windows.net/" 
                media_link = media_link + role_conf.osvhd.media.container
                media_link = media_link + service_conf.name + str(i) + "/" + role_conf.osvhd.media.blob
                osvhd = OSVirtualHardDisk(role_conf.osvhd.image.id, media_link)
                
                if i == 0:
                    result = self.compute.create_vm_deployment(service_conf.name, 
                                    deploymentId,
                                    'production',
                                    role_conf.id + '_' + str(i),
                                    vmconf,
                                    osvhd,
                                    netconf,
                                    role_conf.size)
                else:
                    result = self.compute.append_vm_deployment(service_conf.name,
                                    deploymentId,
                                    role_conf.id + '_' + str(i),
                                    vmconf,
                                    osvhd,
                                    netconf,
                                    role_conf.size)
    
                self.utility.wait_for_async_request(result.request_id)
                props = self.utility.get_deployment_status(service_conf.name, deploymentId)
                self.utility.wait_for_deployment_status(service_conf.name, deploymentId, 'Running')

        except Exception as e:
                print('AZURE ERROR: %s' % str(e))
                print(traceback.format_exc())
                return False

    def delete_role(self, role_conf, service_conf, storage_conf):
        '''
        Deletes the role
        '''

        try:
            deploymentId = uuid.uuid1()
            for i in range(0, role_conf.count):
                vmconf = self.compute.delete_vm_conf(role_conf.id + '_' + str(i))

        except Exception as e:
                print('AZURE ERROR: %s' % str(e))
                print(traceback.format_exc())
                return False
