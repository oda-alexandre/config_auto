# coding:utf-8

'''
module for install gtkhash by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of gtkhash\n \033[0m")

os.system("docker run -d --name gtkhash -v ${HOME}:/home/gtkhash -v /tmp/.X11-unix/:/tmp/.X11-unix/ --pid host --network none -e DISPLAY alexandreoda/gtkhash")
