'''
-Define a class named ssh:
-initialize that class with ip , username, password
-initialize ssh connection using SSHClient()
-set missing host key policy(paramiko.AutoAddPolicy())
-connect to server using connect()
-use transport for channelling purpose
-connect to server for transporting channel

-start a thread after initializing it.


'''
from __future__ import print_function
import threading, paramiko
import os
import time


class ssh:
    client = None
    transport = None
    shell = None

    def __init__(self, address, username, password):
        self.address = address
        self.username = username
        self.password = password

        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        print("Starting SSH connection!")
        self.client.connect(hostname=address,
                            username=username,
                            password=password,
                            port=22,
                            look_for_keys=False)
        print("Connection Established!")
        self.transport = paramiko.Transport(address, 22)
        self.transport.connect(username=username,
                               password=password)

        thread = threading.Thread(target=self.process())
        thread.daemon = True
        thread.start()


    def closeConnection(self):
        if (self.client != None):
            self.client.close()
            self.transport.close()


    def openShell(self):
        self.shell = self.client.invoke_shell()


    def sendShellCommand(self, command):
        if (self.client):
            self.shell.send(command + "\n")
        else:
            print("Shell not opened.")


    def process(self):
        global connection
        PROJECT_PATH = os.path.dirname(os.path.abspath('__file__'))
        BASE_DIR = os.path.dirname(PROJECT_PATH)
        logFileLocation = BASE_DIR+"\LogsDir"+"NewSshDump.log"
        while True:
            if self.shell != None and self.shell.recv_ready():
                alldata = self.shell.recv(1024)
                while self.shell.recv_ready():
                    alldata += self.shell.recv(1024)

                print(alldata)

                with open(logFileLocation, 'a') as logfile:
                    logfile.write(alldata)
            else:
                print("Shell is empty, Nothing to log")


    def loginAsStack(self, username='stack'):
        self.sendShellCommand('sudo su - '+ username+'\n')
        time.sleep(2)
        self.sendShellCommand(self.password+'\n')
        time.sleep(3)
        self.sendShellCommand('cd devstack'+'\n')
        time.sleep(2)
        self.sendShellCommand('./run_test.sh'+'\n')




username = "tellabs"
password = "tellabs$123"
address = "192.168.195.182"


connection = ssh(address, username, password)
connection.openShell()

connection.loginAsStack()
