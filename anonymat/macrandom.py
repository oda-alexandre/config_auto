# coding:utf-8

'''
module for install a script of mac random auto
'''

import os

# INSTALL OF PACKAGES
print("\033[36;1m install prerequisites\n \033[0m")

os.system("sudo apt install --no-install-recommends -y \
git \
macchanger")

# INSTALL SCRIPT /etc/init.d/mac-random
print("\033[36;1m \nSetting up the script\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/mac_random.git && \
sudo mv -f mac_random/mac-random /etc/init.d/ && \
sudo chmod +x /etc/init.d/mac-random")

# AUTO STARTING
os.system("sudo update-rc.d -f mac-random defaults")

# CLEANING OF INSTALL RESIDUES
os.system("rm -rf mac_random")
