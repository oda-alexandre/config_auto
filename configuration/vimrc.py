# coding:utf-8

'''
module pour l'installation de vim avec fichier de configuration personnalisé
'''

import os

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
vim \
git")

# INSTALLATION DU FICHIER /etc/vim/vimrc
print("\033[36;1m \nInstallation du fichier de configuration\n \033[0m")

os.system("git clone https://github.com/oda-alexandre/vimrc.git && \
sudo cp vimrc/vimrc /etc/vim/ && \
rm -rf vimrc")
