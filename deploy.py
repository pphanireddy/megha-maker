#!/usr/bin/python

import os
import fabric.api
import azure

# installs the standard packages required by the service
@fabric.api.task
def install_packages():
    fabric.api.run(r'sudo apt-get install -y python-software-properties')
    fabric.api.run(r'sudo add-apt-repository -y ppa:webupd8team/java')
    fabric.api.run(r'sudo apt-get update')
    fabric.api.run(r'sudo apt-get install -y oracle-java7-installer')

# installs hadoop
@fabric.api.task
def install_hadoop():
    fabric.api.run(r'rm -rf ~/hadoop')
    fabric.api.run(r'wget http://apache.mirrors.spacedump.net/hadoop/common/stable/hadoop-2.5.1.tar.gz')
    fabric.api.run(r'tar xvf hadoop-2.5.1.tar.gz --gzip ~/hadoop')
    fabric.api.run(r'rm hadoop-2.5.1.tar.gz')

# creates the specified service
@fabric.api.task
def create_service(service):
    azure.create_cloudservice(service, 'West US')

# deletes the specified service
@fabric.api.task
def delete_service(service):
    azure.delete_cloudservice(service)
