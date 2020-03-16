# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt update; \
sudo apt install --no-install-recommends -y \
git")

print("\033[36;1m \nSETTING UP SCRIPT\n \033[0m")

print("\033[36;1m \nCREATE FOLDER /usr/share/dict\n \033[0m")

os.system("sudo mkdir /usr/share/dict")

print("\033[36;1m \nINSTALL SCRIPT /etc/init.d/hostname-random & WORDLIST OF NAMES /usr/share/wordlist/names.txt\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/hostname_random.git; \
sudo mv -f hostname_random/names.txt /usr/share/dict/; \
sudo mv -f hostname_random/hostname-random /etc/init.d/; \
sudo chmod +x /etc/init.d/hostname-random")

print("\033[36;1m \nAUTO STARTING\n \033[0m")

os.system("sudo update-rc.d -f hostname-random defaults")

print("\033[36;1m \nCLEANING\n \033[0m")

os.system("rm -rf hostname_random")
