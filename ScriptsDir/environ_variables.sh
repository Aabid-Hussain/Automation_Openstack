#!/usr/bin/env bash

# we can copy and paste openrc files contains here.

export OS_AUTH_URL=
export OS_TENANT_ID=
export OS_TENANT_NAME=
export OS_USERNAME=
# With Keystone you pass the keystone password.
echo "Please enter your OpenStack Password: "
read -s OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT