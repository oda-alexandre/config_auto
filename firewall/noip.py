# coding:utf-8

'''
module for install a script of sync auto of l'ip public with noip
'''

import os

# INSTALL PACKAGES
print("\033[36;1m Install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git \
wget")

# INSTALL OF NOIP
print("\033[36;1m Install of noip\n \033[0m")

os.system("wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz -O && \
noip-duc-linux.tar.gz && \
sudo tar xf noip-duc-linux.tar.gz -C /usr/local/src/")

# MESSAGE
print("\033[36;1m"
      "\n"
      "IN THE WINDOW THAT WILL FOLLOW INQUIRY AS THIS :\n"

      "(FOR CREER A COMPTE NOIP SUIVRE CE LIEN\n" "https://www.noip.com/sign-up)\n"
      "(FOR CREER YOUR COMPTE VIA UNE EMAIL JETABLE SUIVRE CE LIEN\n" "https://www.crazymailing.com/fr/)\n"

      "1-Entrez your email noip\n"
      "2-Enter your password noip\n"
      "3-Entrez y and renseignez the temps entre chaque sync (default 30min)\n"
      "4-Entrez y Appuyez sur entrer\n"
      "\n"
      "\033[0m")

enter = raw_input(
    "\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")

# CONFIG OF NOIP
os.system("sudo make install -C /usr/local/src/noip-*/")

print("\033[36;1m \nSetting up the script\n \033[0m")

# INSTALL SCRIPT /etc/init.d/noip
os.system("git clone https://gitlab.com/oda-alexandre/noip.git noip && \
sudo mv -f noip/noip /etc/init.d/ && \
sudo chmod +x /etc/init.d/noip")

# CLEANING OF INSTALL RESIDUES
os.system("rm -rf noip && \
rm -rf noip-duc-linux.tar.gz && \
sudo rm -rf /usr/local/src/noip-duc-linux.tar.gz")

# LAUNCHING SERVICES AT BOOT
os.system("sudo update-rc.d -f noip defaults && \
sudo service noip start && \
noip2 -U 1")

# MESSAGE
print("\033[36;1m"
      "\n"
      "FOR CHECK THE STATUS TAPER IN A TERMINAL :\n\n"

      "noip2 -S"
      "\n"
      "\033[0m")

enter = raw_input("\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")
