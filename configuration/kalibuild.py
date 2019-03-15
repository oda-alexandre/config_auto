# coding:utf-8

'''
module pour la création d'une ISO kali minimaliste
'''

import os

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
live-build \
cdebootstrap")

# INSTALLATION ET CONFIGURATION DE LIVE BUILD CONFIG AVEC INCLUDES PERSONNALISÉ
print("\033[36;1m \nInstallation et configuration de live-build-config\n \033[0m")

os.system("git clone git://git.kali.org/live-build-config.git && \
cd live-build-config/kali-config/ && \
find . -maxdepth 1 ! -name . ! -name 'variant-default' -exec rm -rf {} \; && \
git clone https://github.com/oda-alexandre/kali_build.git && \
mv kali_build/common ../ && \
mv kali_build/variant-gnome ../ && \
rm -rf kali_build/ && \
cd ../")

# DEMARRAGE DE LA CONSTRUCTION DE L'ISO
print("\033[36;1m \nConstruction de l'iso\n \033[0m")

os.system("sudo ./build.sh --verbose")
