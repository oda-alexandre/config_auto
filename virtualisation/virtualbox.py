# coding:utf-8

'''
module pour l'installation de virtualbox
'''

import os

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install -y \
virtualbox \
virtualbox-ext-pack \
virtualbox-guest-additions-iso")

# AJOUT UTILISATEUR AU GROUPE VBOXUSERS
print("\033[36;1m \nAjout de l'utilisateur au groupe vboxusers\n \033[0m")

os.system("sudo usermod -a -G vboxusers $USER")
