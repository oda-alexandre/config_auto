# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt update && \
sudo apt install -y \
virtualbox \
virtualbox-ext-pack \
virtualbox-guest-additions-iso")

print("\033[36;1m \nADD USER TO GROUP VBOXUSERS\n \033[0m")

os.system("sudo usermod -a -G vboxusers $USER")
