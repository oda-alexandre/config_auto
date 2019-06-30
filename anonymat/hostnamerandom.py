# coding:utf-8

'''
module for install a script of hostname random auto
'''

import os

# INSTALL PACKAGES
print("\033[36;1m \nInstall prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git")

print("\033[36;1m \nSetting up the script\n \033[0m")

# CREATE FOLDER /usr/share/wordlists
os.system("sudo mkdir /usr/share/wordlists")

# INSTALL SCRIPT /etc/init.d/hostname-random & WORDLIST OF NAMES /usr/share/wordlist/names.txt
os.system("git clone https://gitlab.com/oda-alexandre/hostname_random.git && \
sudo mv -f hostname_random/names.txt /usr/share/wordlists/ && \
sudo mv -f hostname_random/hostname-random /etc/init.d/ && \
sudo chmod +x /etc/init.d/hostname-random")

# AUTO STARTING
os.system("sudo update-rc.d -f hostname-random defaults")

# CLEANING
os.system("rm -rf hostname_random")
