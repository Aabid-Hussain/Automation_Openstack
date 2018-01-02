from os import environ
from subprocess import call


call('export OS_TENANT_NAME=admin')
call('export OS_USERNAME=admin')
call('export OS_PASSWORD=ADMIN_PASS')
call('export OS_AUTH_URL=http://controller:35357/v2.0')


def get_nova_credentials_v2():

    dict_container = {}

    dict_container['version'] = '2'
    dict_container['username'] = environ['OS_USERNAME']
    dict_container['api_key'] = environ['OS_PASSWORD']
    dict_container['auth_url'] = environ['OS_AUTH_URL']
    dict_container['project_id'] = environ['OS_TENANT_NAME']

    return dict_container




