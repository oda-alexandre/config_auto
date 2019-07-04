# coding:utf-8

import os

print("\033[36;1m \nINSTALL FROM THE DOCKER HUB\n \033[0m")

os.system("mkdir $HOME/dropbox && \
docker run -d --name dropbox -v ${HOME}/dropbox:/home/dropbox/Dropbox --restart=always alexandreoda/dropbox")
