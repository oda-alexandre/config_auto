# coding:utf-8

import os

print("\033[36;1m \nINSTALL FROM THE DOCKER HUB\n \033[0m")

os.system("docker run --name pelican -p 127.0.0.1:8000:8000  alexandreoda/pelican")
