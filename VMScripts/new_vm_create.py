import os
import time
import novaclient  as nvclients

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

creds = get_nova_creds()
nova = nvclients.client.Client(**creds)

if not nova.keypairs.findall(name="sshkey"):
    with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
        nova.keypairs.create(name="sshkey", public_key=fpubkey.read())


image = nova.images.find(name="cirros")
flavor = nova.flavors.find(name="m1.small")

nova.networks.list()
network = nova.networks.find(label="demo_network1")
nics = [{'net-id': network.id}]

instance = nova.servers.create(name="cirros_test_vm", image='', flavor=flavor, key_name="sshkey", nics=nics)

# Poll at 5 second intervals, until the status is no longer 'BUILD'
status = instance.status
while status == 'BUILD':
    time.sleep(5)
    # Retrieve the instance again so the status field updates
    instance = nova.servers.get(instance.id)
    status = instance.status
print "status: %s" % status
