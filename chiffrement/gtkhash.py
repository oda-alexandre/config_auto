# coding:utf-8

'''
module pour l'installation de gtkhash via docker
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de gtkhash\n \033[0m")

os.system("docker run -d --name gtkhash -v ${HOME}:/home/gtkhash -v /tmp/.X11-unix/:/tmp/.X11-unix/ --pid host --network none -e DISPLAY alexandreoda/gtkhash")
