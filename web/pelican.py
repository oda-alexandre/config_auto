# coding:utf-8

'''
module pour l'installation de pelican via docker
'''

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de pelican\n \033[0m")

os.system("docker run --name pelican -p 127.0.0.1:8000:8000  alexandreoda/pelican")

continue
