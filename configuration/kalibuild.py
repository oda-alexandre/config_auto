# coding:utf-8

'''
module for the build ISO kali minimal
'''

import os

# INSTALL PACKAGES
print("\033[36;1m Install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
live-build \
cdebootstrap")

# INSTALL AND CONFIG OF LIVE BUILD CONFIG WITH INCLUDES CUSTOM
print("\033[36;1m \nInstall and config of live-build-config\n \033[0m")

os.system("git clone git://git.kali.org/live-build-config.git && \
cd live-build-config/kali-config/ && \
find . -maxdepth 1 ! -name . ! -name 'variant-default' -exec rm -rf {} \; && \
git clone https://gitlab.com/oda-alexandre/kali_build.git && \
mv kali_build/common ../ && \
mv kali_build/variant-gnome ../ && \
rm -rf kali_build/ && \
cd ../")

# STARTING THE BUILD OF ISO
print("\033[36;1m \nBuild of iso\n \033[0m")

os.system("sudo ./build.sh --verbose")
