from os import environ, system


#calling .sh script in python using os.system()
system('sh environ_variables.sh')


def get_nova_credentials_v2():

    dict_container = {}

    dict_container['version'] = '2'
    dict_container['username'] = environ['OS_USERNAME']
    dict_container['password'] = environ['OS_PASSWORD']
    dict_container['auth_url'] = environ['OS_AUTH_URL']
    dict_container['project_name'] = environ['OS_TENANT_NAME']

    return dict_container




