# coding:utf-8

import os

print("\033[36;1m \nINSTALL FROM THE DOCKER HUB\n \033[0m")

os.system("docker run -d --name getstation -v ${HOME}:/home/getstation -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -v /etc/localtime:/etc/localtime:ro -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add audio --device /dev/snd  -v /lib/modules:/lib/modules --privileged --network host --cap-add=ALL -e DISPLAY alexandreoda/getstation")
