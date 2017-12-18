from paramiko import client
import os
import time
import sys


HOST_IP = "192.168.195.182"

class ssh:

    def __init__(self, ip, sshUserName, sshPassword):
        self.ip = ip
        self.sshUserName = sshUserName
        self.sshPassword = sshPassword

        self.ssh = client.SSHClient()
        self.ssh.set_missing_host_key_policy(client.AutoAddPolicy)

        try:
            print("SSH connection is started with IP: {}".format(self.ip))
            self.ssh.connect(hostname=ip, username=sshUserName, password=sshPassword, port=22,
                             look_for_keys=False)
            print("SSH connection has established with IP: {}".format(self.ip))

        except client.BadHostKeyException as err:
            print(err)

        except client.SSHException as err:
            print(err)

        except:
            print("Unknown Error!")

    def SendCommand(self, cmd, filename):
        global connection

        PROJECT_PATH = os.path.dirname(os.path.abspath('__file__'))
        BASE_DIR = os.path.dirname(PROJECT_PATH)

        channel = self.ssh.invoke_shell()
        # out = channel.recv(9999)
        channel.send('sudo su - ' + "stack" + '\r\n')
        time.sleep(2)
        channel.send(self.sshPassword + '\r\n')
        time.sleep(3)
        channel.send('cd devstack\r\n')
        time.sleep(1)
        # channel.send('./run_tests.sh\r\n')

        if self.ssh:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)

            while not stdout.channel.exit_status_ready():
                if stdout.channel.recv_ready():
                    data = stdout.channel.recv(100)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(100)
                        data += prevdata
                    filelocation = BASE_DIR+"/LogsDir/"+filename+".log"
                    with open(filelocation, 'a') as output:
                        output.write(data)
                    print(data)
        else:
            print("Connection is closed!")
'''
    def rootcmd1(self, username='default'):
        channel = self.ssh.invoke_shell()
        #out = channel.recv(9999)
        channel.send('sudo su - ' + username + '\r\n')
        time.sleep(2)
        channel.send(self.sshPassword + '\r\n')
        time.sleep(3)
        channel.send('cd devstack\r\n')
        time.sleep(1)
        channel.send('./run_tests.sh\r\n')
        # channel.send('ls -lrt\r\n')
        #max_loops = 5000
        not_done = True
        MAX_BUFFER = 655351
        output = ''
        #i = 0
        sys.stdout.flush()
        sys.stdin.flush()
        sys.stderr.flush()

        PROJECT_PATH = os.path.dirname(os.path.abspath('__file__'))
        BASE_DIR = os.path.dirname(PROJECT_PATH)
        FILELOCATION = BASE_DIR+"/LogsDir/"+"Sshdump.log"

        while not channel.exit_status_ready():
            time.sleep(1)
            
            # Keep reading data as long as available (up to max_loops)
            if channel.recv_ready():
                output = channel.recv(MAX_BUFFER)
                prevdata = b"1"
                while prevdata:
                    prevdata = channel.recv(MAX_BUFFER)
                    output += prevdata

                    with open(FILELOCATION, "a") as dumplog:
                        dumplog.write(output)
                                   # print("Lenght ", len(channel.recv(MAX_BUFFER)))
                print(output)

            else:
                print("Transport channel is unable to receive data")


'''
if __name__ == '__main__':
    connection = ssh(HOST_IP, 'tellabs', 'tellabs$123')
    connection.SendCommand("./run_tests.sh ", 'Sshdump')
    # connection.rootcmd1(username='stack')


