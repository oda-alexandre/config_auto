# coding:utf-8

'''
module for install deamon dropbox by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of dropbox\n \033[0m")

os.system("mkdir $HOME/dropbox && \
docker run -d --name dropbox -v ${HOME}/dropbox:/home/dropbox/Dropbox --restart=always alexandreoda/dropbox")
