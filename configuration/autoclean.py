# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
git")

print("\033[36;1m \nINSTALL SCRIPT /etc/init.d/auto-clean\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/auto_clean.git && \
sudo mv -f auto_clean/auto-clean /etc/init.d/ && \
sudo chmod +x /etc/init.d/auto-clean")

print("\033[36;1m \nAUTO STARTING\n \033[0m")

os.system("sudo update-rc.d -f auto-clean defaults")

print("\033[36;1m \nCLEANING\n \033[0m")

os.system("rm -rf auto_clean")
