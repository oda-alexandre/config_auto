# coding:utf-8

'''
module for install virtualbox
'''

import os

# INSTALL OF PACKAGES
print("\033[36;1m install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install -y \
virtualbox \
virtualbox-ext-pack \
virtualbox-guest-additions-iso")

# ADD USER AU GROUPE VBOXUSERS
print("\033[36;1m \nAjout of user au groupe vboxusers\n \033[0m")

os.system("sudo usermod -a -G vboxusers $USER")
