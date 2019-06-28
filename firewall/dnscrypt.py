# coding:utf-8

'''
module for install dnscrypt by docker
'''

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of dnscrypt\n \033[0m")

os.system("docker run -ti --name dnscrypt --network host --restart=always alexandreoda/dnscrypt")
