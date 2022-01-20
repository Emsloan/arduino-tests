# The purpose of this file is to create a python script that will interact with the
# operating system.  Python automation is a future goal that our sponsor has laid out
# for the team.  The team is trying to get a better understanding of how to utilize python
# to automate interactions between the IDE and user.

import os
import subprocess

# Clear screen command
os.system('CLS')
print('')

# Get python version from the os
os.system("python --version")

# Get name of computer
os.system('hostname')

# Get MAC address of computer
os.system('GETMAC')

# Get system time without prompting a change of the time
os.system('time /t')

# Rename file from system
try:
    os.rename("file.txt", "new_name.txt")
except:
    # if file doesn't exist create it
    file = open('file.txt', 'w')
    file.write('new file')
    file.close()



