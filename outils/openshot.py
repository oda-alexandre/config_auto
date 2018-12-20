# coding:utf-8

'''
module pour l'installation de openshot
'''

import os

# INSTALLATION DE OPENSHOT
print("\033[36;1m \nInstallation de openshot\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
openshot")
