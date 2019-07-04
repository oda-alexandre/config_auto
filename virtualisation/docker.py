# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
gnupg2 \
apt-transport-https \
ca-certificates \
curl \
software-properties-common \
dirmngr")

print("\033[36;1m \nADD REPOS AND KEY GPG\n \033[0m")

os.system("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add - && \
echo \'deb https://download.docker.com/linux/debian stretch stable\' | sudo tee -a /etc/apt/sources.list.d/docker.list")

print("\033[36;1m \nINSTALL DOCKER\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
docker.ce")

print("\033[36;1m \nACTIVATION SERVICE\n \033[0m")

os.system("sudo systemctl start docker.service && \
sudo systemctl enable docker.service")

print("\033[36;1m \nCREATION GROUPE DOCKER\n \033[0m")

os.system("sudo groupadd -f docker")

print("\033[36;1m \nSECURISE RIGHTS SOCK\n \033[0m")

os.system("sudo chown root:docker /var/run/docker.sock")

print("\033[36;1m \nADD USER TO GROUP DOCKER\n \033[0m")

os.system("sudo usermod -a -G docker $USER")

print("\033[36;1m \nSECURISE COMMUNICATIONS INTER CONTENEURS\n \033[0m")

os.system("echo \'DOCKER_OPTS=\"-icc=false\"\' | sudo tee -a /etc/default/docker")

print("\033[36;1m \nREBOOT SERVICE DOCKER\n \033[0m")

os.system("sudo systemctl restart docker.service")

# print("\033[36;1m \nINSTALL PORTAINER\n \033[0m")
#
# os.system("docker run -ti --name portainer -p 127.0.0.1:9000:9000 --restart always -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer")
#
# print("\033[36;1m \nLien to portainer http://localhost:9000\n \033[0m")
#
# enter = raw_input("\033[36;1m \nPush on <Entrée> for confirmer \033[0m")
#
# if enter == "":
#     pass
