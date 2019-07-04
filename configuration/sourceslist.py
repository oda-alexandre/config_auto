# coding:utf-8

'''
module for the config of file /etc/apt/sources.list followed of the mise à level of system
'''

import os

# CHANGE OF FILE /etc/apt/sources.list WITH REPOS contrib non-free
print("\033[36;1m \nChange of file sources.list\n \033[0m")

os.system("sudo rm -f /etc/apt/sources.list && \
echo \"deb https://http.kali.org/kali kali-rolling main contrib non-free\" | sudo tee -a /etc/apt/sources.list && \
echo \"deb-src https://http.kali.org/kali kali-rolling main contrib non-free\" | sudo tee -a /etc/apt/sources.list")

# DIST UPGRADE
print("\033[36;1m \nUpgrade of system\n \033[0m")

os.system("sudo apt update && \
sudo apt upgrade -y && \
sudo apt dist-upgrade -y")

# CLEANING OF SYSTEME
print("\033[36;1m \nCleaning of system\n \033[0m")

os.system("sudo apt-get --purge autoremove -y && \
sudo apt-get autoclean -y")

print("\033[36;1m \nADD ALIAS IN .bashrc\n \033[0m")
print("\033[36;1m \nAdd alias .bashrc\n \033[0m")

os.system("echo \"alias maj=\'sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y && sudo apt-get --purge autoremove -y && sudo apt-get autoclean -y\'\" >> $HOME/.bashrc")
