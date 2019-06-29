# coding:utf-8

'''
module for install a script of ip random auto
'''

import os

# INSTALL PACKAGES
print("\033[36;1m Install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git \
openvpn")

print("\033[36;1m \nSetting up the script\n \033[0m")

# CREATE FOLDER /usr/share/openvpn/vpn
os.system("sudo mkdir /usr/share/openvpn/vpn")

# MESSAGE
print("\033[36;1m" "YOU MUST FILE THE FILES openvpn.conf IN THE FOLDER /usr/share/openvpn/vpn FOR SCRIPT TO WORK\n" "\033[0m")

enter = raw_input("\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")

# INSTALL SCRIPT /etc/init.d/ip-random
os.system("git clone https://gitlab.com/oda-alexandre/ip_random.git && \
sudo mv -f ip_random/ip-random /etc/init.d/ && \
sudo chmod +x /etc/init.d/ip-random")

# LAUNCHING SERVICES AT BOOT
os.system("sudo systemctl restart openvpn && \
sudo systemctl enable openvpn && \
sudo update-rc.d -f ip-random defaults")

# CLEANING OF INSTALL RESIDUES
os.system("rm -rf ip_random")
