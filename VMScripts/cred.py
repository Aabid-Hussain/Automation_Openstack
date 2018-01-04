
#function to store keystone credentials.
def keystone_cred():

    d = {}
    #store information as required by keystone
    d['username'] = 'admin'
    d['password'] = 'openstack123'
    d['auth_url'] = 'http://192.168.195.182:5000/v2.0'
    d['tenant_name'] = 'demo'

    return d

#function to store nova credentials.
def nova_cred():
    d = {}
    #store information as required by nova
    d['auth_url'] = 'http://192.168.195.182:5000/v3'
    d['username'] = 'admin'
    d['password'] = 'openstack123'
    d['project_name'] = 'demo'
    d['version'] = '2'
    return d

