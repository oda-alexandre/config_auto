# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
terminator")

print("\033[36;1m \nINSTALL .bashrc CUSTOM\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/terminal_custom.git && \
cp terminal_custom/bashrc $HOME/.bashrc && \
sudo cp terminal_custom/bashrc /root/.bashrc && \
rm -rf terminal_custom")
