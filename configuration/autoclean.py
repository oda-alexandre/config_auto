# coding:utf-8

'''
module for install a script of cleaning auto
'''

import os

# INSTALL OF PACKAGES
print("\033[36;1m install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git")

# INSTALL SCRIPT /etc/init.d/auto-clean
print("\033[36;1m custom script\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/auto_clean.git && \
sudo mv -f auto_clean/auto-clean /etc/init.d/ && \
sudo chmod +x /etc/init.d/auto-clean")

# AUTO STARTING
os.system("sudo update-rc.d -f auto-clean defaults")

# CLEANING OF INSTALL RESIDUES
os.system("rm -rf auto_clean")
