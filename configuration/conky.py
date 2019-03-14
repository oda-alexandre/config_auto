# coding:utf-8

'''
module pour l'installation de conky avec conky personnalisé
'''

import os

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
psmisc \
conky-manager \
git")

# INSTALLATION DU CONKY PERSONNALISÉ
print("\033[36;1m \nInstallation du conky personnalisé\n \033[0m")

os.system("mkdir $HOME/.conky && \
git clone https://github.com/oda-alexandre/conky.git && \
sudo mv conky/pizzadude_bullets /usr/share/fonts && \
mv conky/conky $HOME/.conky")

# NETTOYAGE DES RESIDUS D'INSTALLATION
os.system("rm -rf conky")

# DEMARRAGE DE CONKY MANAGER
print("\033[36;1m \nDANS LA FENETRE QUI VAS S'OUVRIR SELECTIONNER VOTRE CONKY\n \033[0m")

entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

os.system("conky-manager")
