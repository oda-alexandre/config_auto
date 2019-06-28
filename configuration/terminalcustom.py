# coding:utf-8

'''
module for install terminator and the set up of file .bashrc custom
'''

import os

# INSTALL OF PACKAGES
print("\033[36;1m install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
terminator")

# INSTALL OF FILE .bashrc CUSTOM
print("\033[36;1m \nInstall of file .bashrc\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/terminal_custom.git && \
cp terminal_custom/bashrc $HOME/.bashrc && \
sudo cp terminal_custom/bashrc /root/.bashrc && \
rm -rf terminal_custom")
