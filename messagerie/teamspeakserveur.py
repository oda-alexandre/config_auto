# coding:utf-8

'''
module for install teamspeak serveur by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m \nInstall of teamspeak serveur\n \033[0m")

os.system("docker run -ti --name teamspeak-serveur -p 9987:9987/udp -p 30033:30033 -p 10011:10011 alexandreoda/teamspeak-serveur")
