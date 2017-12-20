from __future__ import print_function
import paramiko
import threading
from AppLogger import LogMessage
import sys

myLog = LogMessage("Sshdump")


class ssh:
    shell = None
    client = None
    transport = None

    def __init__(self, ip, username, password):

        print("Connecting to server on ip ", str(ip))
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        self.client.connect(hostname=ip, username=username, password=password, look_for_keys=False)

        self.transport = paramiko.client.Transport(ip, 22)
        self.transport.connect(username=username, password=password)

        thread = threading.Thread(target=self.process)
        thread.daemon = True
        thread.start()

    def closeConnection(self):
        if(self.client != None):
            self.client.close()
            self.transport.close()

    def openShell(self):
        self.shell = self.client.invoke_shell()

    def sendShell(self, command):
        if(self.shell):
            self.shell.send(command + "\n")
        else:
            print("Shell not opened!")

    def process(self):
        global connection

        while True:
            if self.shell != None and self.shell.recv_ready():
                alldata = self.shell.recv(1024)
                while self.shell.recv_ready():
                    alldata += self.shell.recv(1024)

                strdata = str(alldata)
                strdata.replace("\r", "")
                myLog.log.info(strdata)
                print(strdata, end=" ")

                if (strdata.endswith("$ ")):
                    print("\n$", end=" ")
                sys.exit()

sshUsername = "tellabs"
sshPassword = "tellabs$123"
sshServer = "192.168.195.182"

connection = ssh(sshServer, sshUsername, sshPassword)
connection.openShell()
while True:
    # command = input('$ ')
    # if command.startswith(" "):
    #     command = command[1:]
    connection.sendShell("cd devstack")
    connection.sendShell("./run_tests.sh")



