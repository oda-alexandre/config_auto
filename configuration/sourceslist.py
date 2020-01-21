# coding:utf-8

import os

print("\033[36;1m \nCHANGE OF FILE /etc/apt/sources.list WITH contrib non-free\n \033[0m")

os.system("sudo rm -f /etc/apt/sources.list && \
echo \"deb https://http.kali.org/kali kali-rolling main contrib non-free\" | sudo tee -a /etc/apt/sources.list && \
echo \"deb-src https://http.kali.org/kali kali-rolling main contrib non-free\" | sudo tee -a /etc/apt/sources.list")

print("\033[36;1m \nDIST UPGRADE\n \033[0m")

os.system("sudo apt update && \
sudo apt upgrade -y && \
sudo apt dist-upgrade -y")

print("\033[36;1m \nCLEANING OF SYSTEME\n \033[0m")

os.system("sudo apt-get --purge autoremove -y && \
sudo apt-get autoclean -y")

print("\033[36;1m \nADD ALIAS IN .bashrc\n \033[0m")

os.system("echo \"alias maj=\'sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y && sudo apt-get --purge autoremove -y && sudo apt-get autoclean -y\'\" >> $HOME/.bashrc")
