# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("curl -fsSL https://get.docker.com -o get-docker.sh && \
  sudo sh get-docker.sh")

print("\033[36;1m \nADD USER TO GROUP DOCKER\n \033[0m")

os.system("sudo usermod -a -G docker $USER")

print("\033[36;1m \nREBOOT SERVICE DOCKER\n \033[0m")

os.system("sudo systemctl restart docker.service")