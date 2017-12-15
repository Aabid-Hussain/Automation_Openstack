from paramiko import client
import time

class SshAutomation:

    def __init__(self, ip_add, username, password):
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(hostname=ip_add, username=username, password=password,
                            port=22, look_for_keys=False)
        pass

    def SendCommand(self, cmd):
        if self.client:
            stdin, stdout, stderr = self.client.exec_command(cmd)

            while not stdout.channel.exit_status_ready():
                pass
