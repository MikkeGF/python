
import paramiko
import getpass


pswd = getpass.getpass('Password?')

REMOTE_HOST = '207.154.197.252'
REMOTE_USER = 'mikke'
REMOTE_PASS = pswd


# Remove build files from droplet
def connect_to_droplet():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(REMOTE_HOST, username=REMOTE_USER, password=REMOTE_PASS)
    return client



def execute(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    return stdout



if __name__ == "__main__":
    remote = connect_to_droplet()
    execute(remote, 'rm -rf /var/www/mikkegf.codes/*;')
    output = execute(remote, 'ls -al')
    print(output.readlines())
    print('Success!')
    exit(0)



