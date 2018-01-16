import paramiko
import time
import os


'''
-Define a class named ssh:
-initialize that class with ip , username, password
-initialize ssh connection using SSHClient()
-set missing host key policy(paramiko.AutoAddPolicy())
-connect to server using connect()
-use transport for channelling purpose
-connect to server for transporting channel
'''

def ping_check_for_server(ip_add):
    '''
    check response code equal to 0, if true server is active else server is inactive.
    :param ip_add:
    :return:
    '''
    response = os.system("ping -c 1 " + ip_add)
    if response == 0:
        print("server is Active!")
        return True

    else:
        print("Server is inActive, server required timed out!")
        return False


class SSHAutomation:
    '''
    1. Create a class name SSHAutomation & initialize
    - ip_add
    - username
    - password

    2. Call paramiko.client.SSHClient()
    3. Set set_missing_host_key_policy(client.AutoAddPolicy())
    4. Connect to server with
    - hostname
    - username
    - password
    - port
    - look_for_key
    '''

    def __init__(self, ip_add, username, password):
        self.ip_add = ip_add
        self.username = username
        self.password = password

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:

            self.client.connect(hostname=ip_add, username=username, password=password,
                                look_for_keys=False)

        except paramiko.AuthenticationException as err:
            #print("Authentication error occurred!")
            print(err)

        except paramiko.client. BadHostKeyException as err:
            print(err)

        except paramiko.client.SSHException as err:
            print(err)

        except:
            print("Unknown Error Occurred!")


    def __del__(self):
        if self.client:
            try:
                print("Connection is closing for host {}\n".format(self.ip_add))
                self.client.close()
                self.client = None

            except:
                pass


    def close_connection_host(self):

        '''
        -define close_connection_host(self)
        - use try & except block for capturing any exception
        - close the open connection using close method
        - assign connection attribute to None
        '''
        if self.client:
            try:
                print("Connection is closing for host {}\n".format(self.ip_add))
                self.client.close()
                self.client = None
            except:
                print("Connection is already closed!")
                pass


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

        invoke_shell_command = self.client.invoke_shell()
       #output_of_shell = invoke_shell_command.recv(9999)

        invoke_shell_command.send("sudo su - \n")
        time.sleep(1)
        invoke_shell_command.send(self.password+"\n")
        time.sleep(2)
        invoke_shell_command.send(first_command+"\n")
        time.sleep(1)
        invoke_shell_command.send(second_command+"\n")
        time.sleep(1)

        if set_password:

            invoke_shell_command.send("passwd "+username+"\n")
            time.sleep(0.5)
            invoke_shell_command.send(user_password+"\n")
            time.sleep(0.5)
            invoke_shell_command.send(user_password + "\n")
            time.sleep(0.5)

        while not invoke_shell_command.recv_ready():
            time.sleep(3)

        output_of_shell = invoke_shell_command.recv(9999)
        print(output_of_shell.decode('ascii'))


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
        checker_if_pwd_required = False
        if sudo:
            command = "sudo -S -p '' {}".format(command)
            checker_if_pwd_required = self.password is not None and len(self.password)>0
        stdin, stdout, stderr = self.client.exec_command(command)

        if checker_if_pwd_required:
            stdin.write(self.password+"\n")
            stdin.flush()

        return (stdout.readlines(), stderr.readlines())


    def write_local_conf_data(self, filename, local_conf_data):
        '''
        - define write_local_conf_data(self, filename, data)
        - open SFTPClient session using "open_sftp()"
        - change directory to devstack using chdir()
        - for time being, if error out, mkdir(devstack) and filepath='devstack/'+filename
        - open file in write mode and then write data.
        - use try and except to capture exception properly.
        '''

        self.open_ssh_file_conneciton = self.client.open_sftp()
        file_path = filename

        try:
            try:
                self.open_ssh_file_conneciton.chdir('devstack')

            except IOError:
                self.open_ssh_file_conneciton.mkdir('devstack')
                file_path = 'devstack/'+filename

            with open(file_path, 'w') as file_to_write:
                file_to_write.write(local_conf_data)

        except Exception as err :
            print("***Caught Excpetion as {}:{}".format(err.__class__, err))



if __name__ == '__main__':

    ip_add, username, password = "192.168.195.182", "tellabs", "tellabs$123"

    if ping_check_for_server(ip_add):
        SSHObj = SSHAutomation(ip_add, username, password)
        SSHObj.command_required_root_privilage("df -h", "fdisk -l")
        print(SSHObj.command_required_user_privilage("sudo ls -ltr", sudo=True))

