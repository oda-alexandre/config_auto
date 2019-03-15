# coding:utf-8

'''
module pour l'installation du deamon dropbox via docker
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de dropbox\n \033[0m")

os.system("mkdir $HOME/dropbox && \
docker run -d --name dropbox -v ${HOME}/dropbox:/home/dropbox/Dropbox --restart=always alexandreoda/dropbox")
