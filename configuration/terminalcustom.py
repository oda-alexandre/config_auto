# coding:utf-8

'''
module pour l'installation de terminator et la mise en place du fichier .bashrc personnalisé
'''

import os

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
terminator")

# INSTALLATION DU FICHIER .bashrc PERSONNALISÉ
print("\033[36;1m \nInstallation du fichier .bashrc\n \033[0m")

os.system("git clone https://github.com/oda-alexandre/terminal_custom.git && \
cp terminal_custom/bashrc $HOME/.bashrc && \
sudo cp terminal_custom/bashrc /root/.bashrc && \
rm -rf terminal_custom")
