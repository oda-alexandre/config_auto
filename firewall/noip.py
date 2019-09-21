# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
git \
wget")

print("\033[36;1m \nINSTALL OF NOIP\n \033[0m")

os.system("wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz -O && \
noip-duc-linux.tar.gz && \
sudo tar xf noip-duc-linux.tar.gz -C /usr/local/src/")

print("\033[36;1m"
      "\n"
      "IN THE WINDOW THAT WILL FOLLOW INQUIRY AS THIS :\n"

      "(TO CREATE A COUNT NOIP FOLLOW THIS LINK\n" "https://www.noip.com/sign-up)\n"
      "(FOR CREER YOUR ACCOUNT VIA A DISPOSABLE EMAIL FOLLOW THIS LINK\n" "https://www.crazymailing.com/fr/)\n"

      "1-Enter your email noip\n"
      "2-Enter your password noip\n"
      "3-Enter y and renseignez the time entre chaque sync (default 30min)\n"
      "4-Enter y Push enter\n"
      "\n"
      "\033[0m")

enter = raw_input(
    "\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")

print("\033[36;1m \nCONFIG OF NOIP\n \033[0m")

os.system("sudo make install -C /usr/local/src/noip-*/")

print("\033[36;1m \nINSTALL SCRIPT /etc/init.d/noip\n \033[0m")

os.system("git clone https://gitlab.com/oda-alexandre/noip.git noip && \
sudo mv -f noip/noip /etc/init.d/ && \
sudo chmod +x /etc/init.d/noip")

print("\033[36;1m \nCLEANING\n \033[0m")

os.system("rm -rf noip && \
rm -rf noip-duc-linux.tar.gz && \
sudo rm -rf /usr/local/src/noip-duc-linux.tar.gz")

print("\033[36;1m \nAUTO STARTING\n \033[0m")

os.system("sudo update-rc.d -f noip defaults && \
sudo service noip start && \
noip2 -U 1")

print("\033[36;1m"
      "\n"
      "FOR CHECK THE STATUS TAPE IN A TERMINAL :\n\n"

      "noip2 -S"
      "\n"
      "\033[0m")

enter = raw_input("\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")
