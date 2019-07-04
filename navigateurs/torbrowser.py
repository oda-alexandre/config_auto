# coding:utf-8

import os

print("\033[36;1m \nINSTALL FROM THE DOCKER HUB\n \033[0m")

os.system("mkdir $HOME/tor-browser && \
docker run -d --name tor-browser -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /etc/machine-id:/etc/machine-id:ro -e DISPLAY -v ${HOME}/tor-browser:/home/torbrowser alexandreoda/tor-browser")
