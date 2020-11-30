from paramiko import SSHClient
import getpass
from scp import SCPClient

remote_path = input('Remotepath?')
local_path = input('Local file path?')
pswd = getpass.getpass('Password?')

REMOTE_HOST = '207.154.197.252'
REMOTE_USER = 'mikke'
REMOTE_PASS = pswd

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect(REMOTE_HOST, username=REMOTE_USER, password=REMOTE_PASS)


scp = SCPClient(ssh.get_transport())
scp.put(local_path, remote_path, recursive=True)
scp.close()

