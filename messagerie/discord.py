# coding:utf-8

'''
module for install discord by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of discord\n \033[0m")

os.system("docker run -d --name discord -v ${HOME}:/home/discord -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) -e DISPLAY alexandreoda/discord")
