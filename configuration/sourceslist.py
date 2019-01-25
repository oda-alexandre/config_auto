# coding:utf-8

'''
module pour la configuration du fichier /etc/apt/sources.list suivis de la mise à niveau du systéme
'''

import os

# MODIFICATION DU FICHIER /etc/apt/sources.list AVEC REPOS contrib non-free
print("\033[36;1m \nModification du fichier sources.list\n \033[0m")

os.system("sudo rm -f /etc/apt/sources.list && \
sudo tee -a /etc/apt/sources.list <<EOF
deb https://http.kali.org/kali kali-rolling main contrib non-free
deb-src https://http.kali.org/kali kali-rolling main contrib non-free
EOF")

# MISE A NIVEAU
print("\033[36;1m \nMise à niveau du systéme\n \033[0m")

os.system("sudo apt update && \
sudo apt upgrade -y && \
sudo apt dist-upgrade -y")

# NETTOYAGE DU SYSTEME
print("\033[36;1m \nNettoyage du systéme\n \033[0m")

os.system("sudo apt-get --purge autoremove -y && \
sudo apt-get autoclean -y")

# AJOUT D'UN ALIAS DANS LE .bashrc
print("\033[36;1m \nAjout alias .bashrc\n \033[0m")

os.system("echo \"alias maj=\'sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y && sudo apt-get --purge autoremove -y && sudo apt-get autoclean -y\'\" >> $HOME/.bashrc")
