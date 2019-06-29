# coding:utf-8

'''
module for install android root tools by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of android root tools\n \033[0m")

os.system("docker run -ti --rm --name android-root-tools -v ${HOME}:/home/android -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/bus/usb:/dev/bus/usb --privileged --env=QT_X11_NO_MITSHM=1 -v ${XAUTHORITY}:/xauthority:ro -e XAUTHORITY='/xauthority' -e DISPLAY alexandreoda/android-root-tools")

# ADD A ALIAS IN THE .bashrc
os.system("echo \"alias docker-wifite=\"docker run -ti --rm --name android-root-tools -v ${HOME}:/home/android -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/bus/usb:/dev/bus/usb --privileged --env=QT_X11_NO_MITSHM=1 -v ${XAUTHORITY}:/xauthority:ro -e XAUTHORITY='/xauthority' -e DISPLAY alexandreoda/android-root-tools\"\" >> $HOME/.bashrc")
