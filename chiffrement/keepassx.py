# coding:utf-8

'''
module for install keepassx by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of keepassx\n \033[0m")

os.system("docker run -it --name keepassx --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/keepassx -e DISPLAY -v ${XAUTHORITY}:/xauthority:ro -e XAUTHORITY='/xauthority' --network none alexandreoda/keepassx")
