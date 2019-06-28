# coding:utf-8

'''
module for install transmission by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of transmission\n \033[0m")

os.system("docker run -d --name transmission -v ${HOME}:/home/transmission -v /tmp/.X11-unix/:/tmp/.X11-unix/ -e DISPLAY alexandreoda/transmission")
