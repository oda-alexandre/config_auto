# coding:utf-8

'''
module pour l'installation de htop avec terminal xterm
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de htop\n \033[0m")

os.system("docker run -d --name htop -v ${HOME}:/home/htop -v /tmp/.X11-unix/:/tmp/.X11-unix/ --pid host -e DISPLAY alexandreoda/htop")
