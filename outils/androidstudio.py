# coding:utf-8

'''
module pour l'installation de android studio via docker
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de android studio\n \033[0m")

os.system("docker run -d --name android-studio -v ${HOME}:/home/android-studio -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/bus/usb:/dev/bus/usb --privileged -e DISPLAY alexandreoda/android-studio")
