from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client as nova_client
import time
import argparse


AUTH_URL = 'http://192.168.195.182:5000/v3'
USERNAME = 'admin'
PASSWORD = 'openstack123'
PROJECT_NAME = 'demo'
USER_DOMAIN_NAME = 'Default'
PROJECT_DOMAIN_NAME = 'Default'
NOVA_API_VERSION = '2'


def get_creds():
    credentials = {'auth_url': AUTH_URL, 'username': USERNAME,
                   'password': PASSWORD, 'project_name': PROJECT_NAME,
                   'user_domain_name': USER_DOMAIN_NAME,
                   'project_domain_name':PROJECT_DOMAIN_NAME}
    return credentials


loader = loading.get_plugin_loader('password')
credentials = get_creds()
auth = loader.load_from_options(**credentials)
sess = session.Session(auth=auth)
nova = nova_client.Client(NOVA_API_VERSION, session=sess)

print nova.servers.list()

parser = argparse.ArgumentParser(description="provide vm name to be deleted")
parser.add_argument("--name", type=str, help="provide vm name to be deleted")
args = parser.parse_args()

nova.servers.delete(args.name)
time.sleep(5)
print nova.servers.list()

