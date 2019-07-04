# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
psmisc \
conky-manager \
git")

print("\033[36;1m \nINSTALL OF CONKY CUSTOM\n \033[0m")

os.system("mkdir $HOME/.conky && \
git clone https://gitlab.com/oda-alexandre/conky.git && \
sudo mv conky/pizzadude_bullets /usr/share/fonts && \
mv conky/conky $HOME/.conky")

print("\033[36;1m \nCLEANING\n \033[0m")

os.system("rm -rf conky")

print("\033[36;1m \nSTARTING CONKY MANAGER\n \033[0m")

os.system("conky-manager")
