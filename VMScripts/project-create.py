from keystoneauth1.identity import v2
from keystoneauth1 import session
from keystoneclient.v2_0 import client


username='admin'
password='openstack123'
tenant_name='demo'
auth_url='http://192.168.195.182:5000/v2.0'

auth = v2.Password(username=username, password=password, tenant_name=tenant_name, auth_url=auth_url)

sess = session.Session(auth=auth)
keystone = client.Client(session=sess)

project = keystone.tenants.create(tenant_name="test1", description="Testing Tenant", enabled=True)
print(project)
