# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
tor \
privoxy")

print("\033[36;1m \nCONFIG PRIVOXY\n \033[0m")

os.system("echo \"forward-socks5 / localhost:9050 .\" | sudo tee -a /etc/privoxy/config && \
echo \"forward-socks4 / localhost:9050 .\" | sudo tee -a /etc/privoxy/config && \
echo \"forward-socks4a / localhost:9050 .\" | sudo tee -a /etc/privoxy/config")

print("\033[36;1m"
      "ADD THIS LINES  IN  PARAMETER / NETWORK / PROXY SERVER / MANUAL METHOD :\n\n"

      "HTTP localhost - 8118\n"
      "HTTPS localhost - 8118\n"
      "Socks localhost - 9050\n"
      "\n"
      "\033[0m")

enter = raw_input("\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")

print("\033[36;1m \nDEACTIVATION INTERFACES NETWORK\n \033[0m")

os.system("sudo ifconfig wlan0 down && \
sudo ifconfig eth0 down && \
sudo service network-manager stop")

print("\033[36;1m \nACTIVATION SERVICES TOR & PRIVOXY\n \033[0m")

os.system("sudo update-rc.d -f tor remove && \
sudo update-rc.d -f privoxy remove && \
sudo update-rc.d -f tor defaults && \
sudo update-rc.d -f privoxy defaults && \
sudo update-rc.d -f tor enable && \
sudo update-rc.d -f privoxy enable && \
")

print("\033[36;1m \nREACTIVATION OF THE INTERFACES NETWORK\n \033[0m")

os.system("sudo ifconfig wlan0 up && \
sudo ifconfig eth0 up && \
sudo service network-manager start && \
sudo service privoxy start && \
sudo service tor start")
