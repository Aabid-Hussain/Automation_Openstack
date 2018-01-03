#!/usr/bin/env bash

# we can copy and paste openrc files contains here.

export OS_AUTH_URL=http://192.168.195.182/identity
export OS_TENANT_ID=552a77e5e860429094a47ef7bc6b05c4
export OS_TENANT_NAME="demo"

# unsetting v3 items in case set
unset OS_PROJECT_ID
unset OS_PROJECT_NAME
unset OS_USER_DOMAIN_NAME
unset OS_INTERFACE

export OS_USERNAME="admin"

echo "Please enter your OpenStack Password for project $OS_TENANT_NAME as user $OS_USERNAME: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT

export OS_REGION_NAME="RegionOne"

if [ -z "$OS_REGION_NAME" ]; then unset OS_REGION_NAME; fi

export OS_ENDPOINT_TYPE=publicURL
export OS_IDENTITY_API_VERSION=2
