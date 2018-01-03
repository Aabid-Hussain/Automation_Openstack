# !/usr/bin/env python


import time
from subprocess import call
from novaclient.client import Client
from os import environ, system


#call('credentials.py')
system('sh environ_variables.sh')

def get_nova_credentials_v2():

    dict_container = {}

    dict_container['version'] = '2'
    dict_container['username'] = environ['OS_USERNAME']
    dict_container['password'] = environ['OS_PASSWORD']
    dict_container['auth_url'] = environ['OS_AUTH_URL']
    dict_container['project_name'] = environ['OS_TENANT_NAME']

    return dict_container


try:

    credentials = get_nova_credentials_v2()

    nova_client = Client(**credentials)

    image = nova_client.images.find(name="cirros-0.3.3-x86_64")

    flavor = nova_client.flavors.find(name="m1.tiny")

    net = nova_client.networks.find(label="demo-net")

    #nics = [{'net-id': net.id}]

    instance = nova_client.servers.create(name="vm2", image=image,

                                          flavor=flavor, key_name="demo-key")
                                          #nics=nics)

    print("Sleeping for 5s after create command")

    time.sleep(5)

    print("List of VMs")

    print(nova_client.servers.list())

finally:

    print("Execution Completed")