# coding:utf-8

'''
module pour l'installation du demon snort via docker
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de snort\n \033[0m")

os.system("mkdir $HOME/snort && \
docker run -it --name snort -v ${HOME}/snort:/snort -v ${HOME}/snort:/etc/snort -v ${HOME}/snort:/usr/local/lib -v ${HOME}/snort:/var/log/snort --network host --cap-add=NET_ADMIN --restart=always alexandreoda/snort")
