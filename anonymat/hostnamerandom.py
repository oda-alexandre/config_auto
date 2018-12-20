# coding:utf-8

'''
module pour l'installation d'un script de hostname aléatoire automatique
'''

import os

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git")

print("\033[36;1m \nMise en place du script\n \033[0m")

# CREATION DU DOSSIER /usr/share/wordlists
os.system("sudo mkdir /usr/share/wordlists")

# INSTALLATION DU SCRIPT /etc/init.d/hostname-random & DE LA WORDLIST DE NOMS /usr/share/wordlist/names.txt
os.system("git clone https://github.com/oda-alexandre/hostname_random.git && \
sudo mv -f hostname_random/names.txt /usr/share/wordlists/ && \
sudo mv -f hostname_random/hostname-random /etc/init.d/ && \
sudo chmod +x /etc/init.d/hostname-random")

# LANCEMENT DU SERVICE AU DEMARRAGE
os.system("sudo update-rc.d -f hostname-random defaults")

# NETTOYAGE DES RESIDUS D'INSTALLATION
os.system("rm -rf hostname_random")
