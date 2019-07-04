# coding:utf-8

'''
module for install android root tools by docker
'''

import os

print("\033[36;1m \nINSTALL FROM THE DOCKER HUB\n \033[0m")

os.system("docker run -ti --rm --name adb-fastboot -v ${HOME}:/home/android -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/bus/usb:/dev/bus/usb --privileged --env=QT_X11_NO_MITSHM=1 -v ${XAUTHORITY}:/xauthority:ro -e XAUTHORITY='/xauthority' -e DISPLAY alexandreoda/adb-fastboot")

print("\033[36;1m \nADD ALIAS IN .bashrc\n \033[0m")

os.system("echo \"alias docker-wifite=\"docker run -ti --rm --name adb-fastboot -v ${HOME}:/home/android -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/bus/usb:/dev/bus/usb --privileged --env=QT_X11_NO_MITSHM=1 -v ${XAUTHORITY}:/xauthority:ro -e XAUTHORITY='/xauthority' -e DISPLAY alexandreoda/adb-fastboot\"\" >> $HOME/.bashrc")
