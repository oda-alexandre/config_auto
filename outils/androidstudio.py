# coding:utf-8

'''
module for install android studio by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of android studio\n \033[0m")

os.system("docker run -d --name android-studio -v ${HOME}:/home/android-studio -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/bus/usb:/dev/bus/usb --privileged -e DISPLAY alexandreoda/android-studio")
