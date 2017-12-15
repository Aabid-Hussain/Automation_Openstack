from paramiko import client
import time
import os

HOST_IP_ADDRESS = "192.168.195.182"

def ServerPingCheck(ip_add):
    response = os.system("ping -c 1 " + ip_add)
    if response:
        return True
    else:
        return False


class SshAutomation:
    client = None

    def __init__(self, ip_add, username, password):

        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(hostname=ip_add, username=username, password=password,
                            port=22, look_for_keys=False)


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
            print("There is no connection exist.")


if __name__ == '__main__':

    print("Checking ping status")
    if ServerPingCheck(HOST_IP_ADDRESS):
        print("Server connection started")
        fob = SshAutomation(HOST_IP_ADDRESS, "tellabs", "tellabs$123")

        fob.SendCommand("compgen -u")
        print("Connection terminated")
    
    else:
        print("Server is timeout, please fix this issue")