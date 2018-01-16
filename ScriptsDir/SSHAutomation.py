#! /usr/bin/env python

# from paramiko import client
import time
import paramiko
import os
from AppLogger import LogMessage
import socket



HOST_IP_ADDRESS = "192.168.195.182"

myLog = LogMessage("EventLogger")

#Function defined to print output and log events
def logPrint(str):
    print(str)
    myLog.log.info(str)

#function defined to verify ping for host
def ServerPingCheck(ip_add):
    response = os.system("ping -c 1 " + ip_add)
    print("\n\r")
    time.sleep(2)

    if response == 0:
        logPrint("ping for {} is successful".format(ip_add))
        return True
    else:
        return False

#class defined for SSH to host
class SSHAutomation:
    '''
        -Define a class named SSHAutomation:
        -initialize that class with ip_add , username, password
        -initialize ssh connection using SSHClient()
        -set missing host key policy(paramiko.AutoAddPolicy())
        -connect to server using connect(hostname=, username=, password=, port=, look_for_keys=)
        -use transport to set channel for logging. this is used by default.
        -connect to server for transporting channel
        #-start a thread after initializing it.
    '''
    client = None

    def __init__(self, ip_add, username, password):
        self.ip_add = ip_add
        self.username = username
        self.password = password

        #initialize SSH connection
        self.client = paramiko.SSHClient()

        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(hostname=ip_add, username=username, password=password,
                                port=22, look_for_keys=False)

        except paramiko.client.BadHostKeyException:
            logPrint("couldn't verified HostKey in server")

        except paramiko.AuthenticationException:
            logPrint("Authentication Failed")
            quit()

        except paramiko.SSHException:
            logPrint("Connection Failed")
            quit()

        except:
            logPrint("Unknown Error")

        #To load host_keys from system
        try:
            self.client.load_system_host_keys()
            logPrint("SSH_keys has been read from 'known hosts' file of user: {}".format(socket.gethostname()))

        except IOError as err:
            '''IOError: 
                        it is raised when file is provided but file is unable to read
            '''
            logPrint(err)


    def close_connection_host(self):
        '''
        -define close_connection_host(self)
        - use try & except block for capturing any exception
        - close the open connection using close method
        - assign connection attribute to None
        '''
        if self.client:
            try:
                logPrint("Connection is closing for IP: {}".format(self.ip_add))
                self.client.close()
                self.client = None

            except IOError as err:
                logPrint(err)


    def command_required_root_privilage(self, first_command, second_command,
                                        set_password=False, user_password='root', username='default'):

        '''
        define command_required_root_privilege(self,
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
        '''
        shell_command_invoke = self.client.invoke_shell()
        shell_command_invoke.send("sudo su - \n")
        time.sleep(2)

        shell_command_invoke.send(self.password + "\n")
        time.sleep(2)

        shell_command_invoke.send(first_command + "\n")
        time.sleep(2)

        shell_command_invoke.send(second_command + "\n")
        time.sleep(2)

        if set_password:
            shell_command_invoke.send("passwd " + username + "\n")
            shell_command_invoke.send(user_password + "\n")
            time.sleep(0.5)
            shell_command_invoke.send(user_password + "\n")

        while not shell_command_invoke.recv_ready():
            time.sleep(3)

        output_of_shell = shell_command_invoke.recv(999999)
        logPrint(output_of_shell.decode('ascii'))


    def command_required_user_privilage(self, command, sudo=False):
        '''
        define command_required_user_privilege(self, command, sudo=False)
            -if user provide commands requires sudo permission then we need to pass password.
            - one way to deal this problem is using
                sudo -S -p '' sudo ls -ltr
            -p: prompt, use a custom password prompt with optional escape sequence[%].
            -S: --stdin, write the prompt to the standard error
                 and read the password from the standard input
                 instead of using the terminal device.
                 The password must be followed by a newline character.
            - use exec_command(command) to store stdin, stdout & stderr
            - if password exist the write the password to stdin and then flush once it is used.
            - return(stdout.readlines(), stderr.readlines())
        '''


    def write_local_conf_data(self, filename, local_conf_data):
        '''
        - define write_local_conf_data(self, filename, data)
        - open SFTPClient session using "open_sftp()"
        - change directory to devstack using chdir()
        - for time being, if error out, mkdir(devstack) and filepath='devstack/'+filename
        - open file in write mode and then write data.
        - use try and except to capture exception properly.
        '''



    def SendCommand(self, cmd):
        if self.client:
            stdin, stdout, stderr = self.client.exec_command(cmd)

            while not stdout.channel.exit_status_ready():
                if stdout.channel.recv_ready():
                    data = stdout.channel.recv(10)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(10)
                        data += prevdata
                    print(data)
        else:
            logPrint("There is no connection exist.")




if __name__ == '__main__':

    logPrint("Checking ping status\n\n\n")

    if ServerPingCheck(HOST_IP_ADDRESS):
        logPrint("Server connection started")
        fob = SSHAutomation(HOST_IP_ADDRESS, "tellabs", "tellabs$123")

        fob.SendCommand("compgen -u")
        logPrint("Connection terminated")

    else:
        logPrint("!!!Server is timed out, please fix connection issue on priority!!!")