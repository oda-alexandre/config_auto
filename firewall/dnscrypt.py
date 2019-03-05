# coding:utf-8

'''
module pour l'installation de dnscrypt via docker
'''

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de dnscrypt\n \033[0m")

os.system("docker run -ti --name dnscrypt --network host --restart=always alexandreoda/dnscrypt")
