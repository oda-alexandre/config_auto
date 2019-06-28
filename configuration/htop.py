# coding:utf-8

'''
module for install htop with terminal xterm
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of htop\n \033[0m")

os.system("docker run -d --name htop -v ${HOME}:/home/htop -v /tmp/.X11-unix/:/tmp/.X11-unix/ --pid host -e DISPLAY alexandreoda/htop")
