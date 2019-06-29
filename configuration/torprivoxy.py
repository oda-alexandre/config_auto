# coding:utf-8

'''
module for install tor and of privoxy
'''

import os

# INSTALL PACKAGES
print("\033[36;1m Install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
tor \
privoxy")

# CONFIG OF FILE /etc/privoxy/config
print("\033[36;1m \nConfiguration\n \033[0m")

os.system("echo \"forward-socks5 / localhost:9050 .\" | sudo tee -a /etc/privoxy/config && \
echo \"forward-socks4 / localhost:9050 .\" | sudo tee -a /etc/privoxy/config && \
echo \"forward-socks4a / localhost:9050 .\" | sudo tee -a /etc/privoxy/config")

# CONFIG MANUAL OF NETWORK
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

# DEACTIVATION OF THE INTERFACES NETWORK
print("\033[36;1m \nDeactivation of the network\n \033[0m")

os.system("sudo ifconfig wlan0 down && \
sudo ifconfig eth0 down && \
sudo service network-manager stop")

# ACTIVATION OF THE SERVICES TOR & PRIVOXY
print("\033[36;1m \nActivation of the services\n \033[0m")

os.system("sudo update-rc.d -f tor remove && \
sudo update-rc.d -f privoxy remove && \
sudo update-rc.d -f tor defaults && \
sudo update-rc.d -f privoxy defaults && \
sudo update-rc.d -f tor enable && \
sudo update-rc.d -f privoxy enable && \
")

# REACTIVATION OF THE INTERFACES NETWORK
print("\033[36;1m \nRéactivation of the network\n \033[0m")

os.system("sudo ifconfig wlan0 up && \
sudo ifconfig eth0 up && \
sudo service network-manager start && \
sudo service privoxy start && \
sudo service tor start")
