# coding:utf-8

'''
module for activation of bluetooth
'''

import os

# INSTALL PACKAGES
print("\033[36;1m Install prerequisites\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
bluetooth \
gnome-bluetooth \
pulseaudio-module-bluetooth")

# AUTO STARTING
print("\033[36;1m \nService activation at boot\n \033[0m")

os.system("sudo systemctl enable bluetooth.service && \
sudo systemctl start bluetooth.service")
