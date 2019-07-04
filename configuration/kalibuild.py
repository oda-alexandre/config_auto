# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
live-build \
cdebootstrap")

print("\033[36;1m \nINSTALL AND CONFIG LIVE BUILD WITH INCLUDES CUSTOM\n \033[0m")

os.system("git clone git://git.kali.org/live-build-config.git && \
cd live-build-config/kali-config/ && \
find . -maxdepth 1 ! -name . ! -name 'variant-default' -exec rm -rf {} \; && \
git clone https://gitlab.com/oda-alexandre/kali_build.git && \
mv kali_build/common ../ && \
mv kali_build/variant-gnome ../ && \
rm -rf kali_build/ && \
cd ../")


print("\033[36;1m \nSTARTING BUILD\n \033[0m")

os.system("sudo ./build.sh --verbose")
