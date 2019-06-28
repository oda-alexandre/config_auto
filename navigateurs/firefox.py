# coding:utf-8

'''
module for install firefox by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of firefox\n \033[0m")

os.system("docker run -d --name firefox -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) -v ${HOME}:/home/firefox -e DISPLAY --network host alexandreoda/firefox")
