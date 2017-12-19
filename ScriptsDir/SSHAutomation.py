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
        logPrint("Server is timeout, please fix connection issue on priority")