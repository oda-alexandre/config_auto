# coding:utf-8

'''
module for install teamspeak client by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m \nInstall of teamspeak client\n \033[0m")

os.system("docker run -ti --name teamspeak-client -v ${HOME}/Downloads:/home/teamspeak/Downloads --env=QT_X11_NO_MITSHM=1 -v ${XAUTHORITY}:/xauthority:ro -e XAUTHORITY='/xauthority' -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -v /etc/localtime:/etc/localtime:ro -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) -e DISPLAY alexandreoda/teamspeak-client")
