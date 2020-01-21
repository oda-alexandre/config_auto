# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
git \
openvpn")

print("\033[36;1m \nSETTING UP SCRIPT\n \033[0m")

os.system("sudo mkdir /usr/share/openvpn/vpn")

print("\033[36;1m" "YOU MUST FILE THE FILES openvpn.conf IN THE FOLDER /usr/share/openvpn/vpn FOR SCRIPT TO WORK\n" "\033[0m")

enter = raw_input("\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")

print("\033[36;1m \nINSTALL SCRIPT /etc/init.d/ip-random\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/ip_random.git && \
sudo mv -f ip_random/ip-random /etc/init.d/ && \
sudo chmod +x /etc/init.d/ip-random")

print("\033[36;1m \nAUTO STARTING\n \033[0m")

os.system("sudo systemctl restart openvpn && \
sudo systemctl enable openvpn && \
sudo update-rc.d -f ip-random defaults")

print("\033[36;1m \nCLEANING\n \033[0m")

os.system("rm -rf ip_random")
