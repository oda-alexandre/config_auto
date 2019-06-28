# coding:utf-8

'''
module for install peazip by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of peazip\n \033[0m")

os.system("docker run -d --name peazip -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/peazip -e DISPLAY --network none alexandreoda/peazip")
