import os

# input use

# local_path = input('local path?')
# remote_path = input('Remote path?')

# paths saved to variable
local_path = '/home/mikkegf/Development/schoolsite/build/*'
remote_path = '/var/www/mikkegf.codes'


REMOTE_HOST = '207.154.197.252'
REMOTE_USER = 'mikke'


os.system(f"scp -r {local_path} {REMOTE_USER}@{REMOTE_HOST}:{remote_path}")