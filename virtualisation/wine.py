# coding:utf-8

'''
module for install wine by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of wine\n \033[0m")

os.system("docker run --rm -ti --name wine -v ${HOME}:/home/wine -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -v /etc/localtime:/etc/localtime:ro -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) -e DISPLAY alexandreoda/wine")

# ADD A ALIAS  IN  THE .bashrc
print("\033[36;1m \nCréation d'un alias  in  the .bashrc\n \033[0m")

os.system("echo \"alias docker-wine=\'docker run --rm -ti --name wine -v ${HOME}:/home/wine -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -v /etc/localtime:/etc/localtime:ro -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) -e DISPLAY alexandreoda/wine\'\" >> $HOME/.bashrc")
