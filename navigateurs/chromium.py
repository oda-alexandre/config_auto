# coding:utf-8

'''
module pour l'installation de chromium via docker
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de chromium\n \033[0m")

os.system("docker run -d --name chromium -v ${HOME}:/home/chromium -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) --network host -e DISPLAY alexandreoda/chromium")
