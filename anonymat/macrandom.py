# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt install --no-install-recommends -y \
git \
macchanger")

print("\033[36;1m \nINSTALL SCRIPT /etc/init.d/mac-random\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/mac_random.git; \
sudo mv -f mac_random/mac-random /etc/init.d/; \
sudo chmod +x /etc/init.d/mac-random")

print("\033[36;1m \nAUTO STARTING\n \033[0m")

os.system("sudo update-rc.d -f mac-random defaults")

print("\033[36;1m \nCLEANING\n \033[0m")

os.system("rm -rf mac_random")
