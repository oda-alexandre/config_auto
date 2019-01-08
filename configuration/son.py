# coding:utf-8

'''
module pour l'activation du son
'''

import os

# INSTALLATION DE PULSEAUDIO
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
*pulseaudio")
