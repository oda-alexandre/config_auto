# coding:utf-8

import os

print("\033[36;1m \nINSTALL FROM THE DOCKER HUB\n \033[0m")

os.system("docker run -d --name teamviewer -e DISPLAY -e XAUTHORITY=${XAUTHORITY} -v /tmp/.X11-unix:/tmp/.X11-unix hurricane/teamviewer")
