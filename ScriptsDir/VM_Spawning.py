import os


'''
export OS_TENANT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=ADMIN_PASS
export OS_AUTH_URL=http://controller:35357/v2.0
'''

def get_nova_credentials_v2():

    d = {}

    d['version'] = '2'

    d['username'] = os.environ['OS_USERNAME']

    d['api_key'] = os.environ['OS_PASSWORD']

    d['auth_url'] = os.environ['OS_AUTH_URL']

    d['project_id'] = os.environ['OS_TENANT_NAME']

    return d


# !/usr/bin/env python

import time
from subprocess import call
import os


call('credentials.py')

from novaclient.client import Client

try:

    credentials = get_nova_credentials_v2()

    nova_client = Client(**credentials)

    image = nova_client.images.find(name="cirros-0.3.3-x86_64")

    flavor = nova_client.flavors.find(name="m1.tiny")

    net = nova_client.networks.find(label="demo-net")

    nics = [{'net-id': net.id}]

    instance = nova_client.servers.create(name="vm2", image=image,

                                          flavor=flavor, key_name="demo-key", nics=nics)

    print("Sleeping for 5s after create command")

    time.sleep(5)

    print("List of VMs")

    print(nova_client.servers.list())

finally:

    print("Execution Completed")