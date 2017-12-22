import paramiko
import time
import os



def ping_check_for_server(ip_add):

    response = os.system("ping -c 1 " + ip_add)
    if response == 0:
        print("server is Active!")

    else:
        print("Server is inActive, server required timed out!")
'''
-Define a class named ssh:
-initialize that class with ip , username, password
-initialize ssh connection using SSHClient()
-set missing host key policy(paramiko.AutoAddPolicy())
-connect to server using connect()
-use transport for channelling purpose
-connect to server for transporting channel

-start a thread after initializing it.

1. Create a class name SSHAutomation & initialize
    - ip_add
    - username
    - password

2. call paramiko.client.SSHClient()
3. set set_missing_host_key_policy(client.AutoAddPolicy())
4. Connect to server with
    - hostname
    - username
    - password
    - port
    - look_for_key

5. define close_connection_host(self)
    - use try & except block for capturing any exception
    - close the open connection using close method
    - assign connection attribute to None

6. define command_required_root_privilege(self,
        set_password=False, password='root',
        first_command, second_command, username='default'
        )
     -invoke_shell() and send following command
        - send "sudo su - \n" and sleep for 2secs
        - send password to enable sudo and sleep for 2secs
        - send first_command and sleep for 2secs
        - send second_command and sleep for 2secs
        - check set_password if True then
            -change the password using command "passwd username"
            -send password and sleep for 2 secs
            -send confirmation password again and sleep for 2secs
    - check if channel is ready to receive data else sleep for 5secs
    - receive the data and store it in output variable
    - finally decode the output in utf-8 or ascii and print or log it.

7. define command_required_user_privilege(self, command,
                        sudo=False)
    -if user provide commands requires sudo permission then
        we need to pass password.
    - one way to deal this problem is using
        sudo -S -p '' sudo ls -ltr
        -p: prompt, use a custom password prompt with optional escape sequence[%].
        -S: --stdin, write the prompt to the standard error
         and read the password from the standard input
         instead of using the terminal device.
         The password must be followed by a newline character.
    - use exec_command(command) to store stdin, stdout & stderr
    - if password exist the write the password to stdin and then flush once it is used.
    return(stdout.readlines(), stderr.readlines())

8. define write_local_conf_data(self, filename, data)
    - open SFTPClient session using "open_sftp()"
    - change directory to devstack using chdir()
    - for time being, if error out, mkdir(devstack) and filepath='devstack/'+filename
    - open file in write mode and then write data.
    -use try and except to capture exception properly.


'''


class SSHAutomation:

    def __init__(self, ip_add, username, password):
        self.ip_add = ip_add
        self.username = username
        self.password = password

        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy)

        try:

            self.client.connect(hostname=ip_add, username=username, password=password,
                                port=22, look_for_keys=False)

        except paramiko.AuthenticationException as err:
            print("Authentication error occured!")
            print(err)

        except paramiko.client. BadHostKeyException as err:
            print(err)

        except paramiko.client.SSHException as err:
            print(err)
        except:
            print("Unknown Error Occured!")


    def close_connection_host(self, first_command, second_command,
                              username='default', set_password=False,
                              password='root'):

        pass


    def command_required_root_privilage(self):
        pass

    def command_required_user_privilage(self):
        pass

    def write_local_conf_data(self):
        pass


if __name__ == '__main__':

    ip_add, username, password = "192.168.195.182", "tellabs", "openstack123"
    SSHObj = SSHAutomation(ip_add, username, password)
    SSHObj.command_required_root_privilage()

