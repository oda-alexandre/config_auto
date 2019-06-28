# coding:utf-8

'''
module for install teamviewer by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of teamviewer\n \033[0m")

os.system("docker run -d --name teamviewer -e DISPLAY -e XAUTHORITY=${XAUTHORITY} -v /tmp/.X11-unix:/tmp/.X11-unix hurricane/teamviewer")
