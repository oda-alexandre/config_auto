# coding:utf-8

'''
module pour l'installation de peazip via docker
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de peazip\n \033[0m")

os.system("docker run -d --name peazip -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/peazip -e DISPLAY --network none alexandreoda/peazip")
