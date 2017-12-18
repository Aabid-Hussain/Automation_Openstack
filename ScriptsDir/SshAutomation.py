# from paramiko import client
import time
import paramiko
import os

HOST_IP_ADDRESS = "192.168.195.182"

def ServerPingCheck(ip_add):
    response = os.system("ping -c 1 " + ip_add)
    print("\n\r")
    time.sleep(2)
    if response == 0:
        print("ping for {} is successful".format(ip_add))
        return True
    else:
        return False


class SshAutomation:
    client = None

    def __init__(self, ip_add, username, password):

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(hostname=ip_add, username=username, password=password,
                            port=22, look_for_keys=False)

        except paramiko.AuthenticationException:
            print("Authentication Failed")
            quit()

        except paramiko.SSHException:
            print("Connection Failed")
            quit()

        except:
            print("Unknown Error")

        self.client.load_system_host_keys()


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