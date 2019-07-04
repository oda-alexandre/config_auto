# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
bluetooth \
gnome-bluetooth \
pulseaudio-module-bluetooth")

print("\033[36;1m \nAUTO STARTING\n \033[0m")

os.system("sudo systemctl enable bluetooth.service && \
sudo systemctl start bluetooth.service")
