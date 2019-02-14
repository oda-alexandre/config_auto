# coding:utf-8

'''
module pour l'installation d'un script d'ip aléatoire automatique
'''

import os

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git \
openvpn")

print("\033[36;1m \nMise en place du script\n \033[0m")

# CREATION DU DOSSIER /usr/share/openvpn/vpn
os.system("sudo mkdir /usr/share/openvpn/vpn")

# MESSAGE
print("\033[36;1m" "VOUS DEVEZ METTRE LES FICHIERS openvpn.conf DANS LE DOSSIER /usr/share/openvpn/vpn POUR QUE LE SCRIPT FONCTIONNE\n" "\033[0m")

entree = input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

# INSTALLATION DU SCRIPT /etc/init.d/ip-random
os.system("git clone https://github.com/oda-alexandre/ip_random.git && \
sudo mv -f ip_random/ip-random /etc/init.d/ && \
sudo chmod +x /etc/init.d/ip-random")

# LANCEMENT DES SERVICES AU DEMARRAGE
os.system("sudo systemctl restart openvpn && \
sudo systemctl enable openvpn && \
sudo update-rc.d -f ip-random defaults")

# NETTOYAGE DES RESIDUS D'INSTALLATION
os.system("rm -rf ip_random")
