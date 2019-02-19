# coding:utf-8

'''
module pour l'installation de teamspeak serveur via docker
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallations de teamspeak serveur\n \033[0m")

os.system("docker run -ti --name teamspeak-serveur -p 9987:9987/udp -p 30033:30033 -p 10011:10011 alexandreoda/teamspeak-serveur")
