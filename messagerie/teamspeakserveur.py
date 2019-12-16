# coding:utf-8

import os

print("\033[36;1m \nINSTALL FROM THE DOCKER HUB\n \033[0m")

os.system("docker run -ti --rm --name teamspeak-serveur -p 9987:9987/udp -p 30033:30033 -p 10011:10011 alexandreoda/teamspeak-serveur")
