# coding:utf-8

'''
module for install libreoffice by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of libreoffice\n \033[0m")

os.system("docker run -d --name libreoffice -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/libreoffice -e DISPLAY --network none alexandreoda/libreoffice")
