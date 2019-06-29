# coding:utf-8

'''
module for install virtualbox
'''

import os

# INSTALL PACKAGES
print("\033[36;1m Install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install -y \
virtualbox \
virtualbox-ext-pack \
virtualbox-guest-additions-iso")

# ADD USER TO THE GROUP VBOXUSERS
print("\033[36;1m \nAdd of user to the group vboxusers\n \033[0m")

os.system("sudo usermod -a -G vboxusers $USER")
