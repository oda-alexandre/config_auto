# coding:utf-8

'''
module for install atom by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of atom\n \033[0m")

os.system("docker run -d --name atom -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/atom -e DISPLAY alexandreoda/atom")
