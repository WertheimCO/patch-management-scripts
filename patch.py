import os
import subprocess

# Check for available system updates
def check_for_updates():
    command = 'apt-get update -y && apt-get upgrade -s'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode()

# Install available updates
def install_updates():
    command = 'apt-get upgrade -y'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode()

# Check if script is running with root privileges
if os.geteuid() != 0:
    print('This script must be run with root privileges.')
    exit()

# Check for and install available updates
updates = check_for_updates()
if 'upgraded' in updates:
    print('Updates are available:')
    print(updates)
    answer = input('Do you want to install them? [y/n] ')
    if answer.lower() == 'y':
        install_updates()
        print('Updates have been installed.')
    else:
        print('Updates have not been installed.')
else:
    print('No updates are available.')
