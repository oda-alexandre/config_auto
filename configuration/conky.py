# coding:utf-8

'''
module for install conky with conky custom
'''

import os

# INSTALL PACKAGES
print("\033[36;1m Install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
psmisc \
conky-manager \
git")

# INSTALL OF CONKY CUSTOM
print("\033[36;1m \nInstall conky custom\n \033[0m")

os.system("mkdir $HOME/.conky && \
git clone https://gitlab.com/oda-alexandre/conky.git && \
sudo mv conky/pizzadude_bullets /usr/share/fonts && \
mv conky/conky $HOME/.conky")

# CLEANING OF INSTALL RESIDUES
os.system("rm -rf conky")

# STARTING CONKY MANAGER
print("\033[36;1m \n IN THE WINDOW SELECT YOUR CONKY\n \033[0m")

enter = raw_input("\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")

os.system("conky-manager")
