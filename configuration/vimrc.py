# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
vim \
git")

print("\033[36;1m \nINSTALL FILE /etc/vim/vimrc\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/vimrc.git && \
sudo cp vimrc/vimrc /etc/vim/ && \
rm -rf vimrc")
