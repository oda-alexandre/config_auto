# coding:utf-8

'''
module for install pelican by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m Install of pelican\n \033[0m")

os.system("docker run --name pelican -p 127.0.0.1:8000:8000  alexandreoda/pelican")
