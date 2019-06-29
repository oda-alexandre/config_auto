# coding:utf-8

'''
module for install vim with file of config custom
'''

import os

# INSTALL PACKAGES
print("\033[36;1m Install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
vim \
git")

# INSTALL OF FILE /etc/vim/vimrc
print("\033[36;1m \nInstall of file of config\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/vimrc.git && \
sudo cp vimrc/vimrc /etc/vim/ && \
rm -rf vimrc")
