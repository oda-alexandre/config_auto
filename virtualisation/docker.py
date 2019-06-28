# coding:utf-8

'''
module for install docker
'''

import os

# INSTALL OF PACKAGES
print("\033[36;1m install prerequisites\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
gnupg2 \
apt-transport-https \
ca-certificates \
curl \
software-properties-common \
dirmngr")

# AJOUT OF REPOS AND OF THE CLEF GPG
print("\033[36;1m \nAjout of repos and of the clef gpg\n \033[0m")

os.system("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add - && \
echo \'deb https://download.docker.com/linux/debian stretch stable\' | sudo tee -a /etc/apt/sources.list.d/docker.list")

# INSTALL OF DOCKER
print("\033[36;1m Install of docker\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
docker.ce")

# ACTIVATION OF SERVICE
print("\033[36;1m \nService activation at boot\n \033[0m")

os.system("sudo systemctl start docker.service && \
sudo systemctl enable docker.service")

# CREATION OF GROUPE DOCKER
print("\033[36;1m \nCréation of groupe docker\n \033[0m")

os.system("sudo groupadd -f docker")

# SECURISATION OF THE DROITS SOCK
print("\033[36;1m \nSécurisation of the droits sock\n \033[0m")

os.system("sudo chown root:docker /var/run/docker.sock")

# AJOUT OF L'USER AU GROUPE DOCKER
print("\033[36;1m \nAjout of user au groupe docker\n \033[0m")

os.system("sudo usermod -a -G docker $USER")

# SECURISATIONS OF THE COMMUNICATIONS INTER CONTENEURS
print("\033[36;1m \nIsolation of the communications inter-conteneurs\n \033[0m")

os.system("echo \'DOCKER_OPTS=\"-icc=false\"\' | sudo tee -a /etc/default/docker")

# REDEMARRAGE OF SERVICE DOCKER
print("\033[36;1m \nRestart-up of service\n \033[0m")

os.system("sudo systemctl restart docker.service")

# INSTALL OF L'INTERFACE GRAPHIQUE PORTAINER DEPUIS THE DOCKER HUB
print("\033[36;1m \nInstall of gestionnaire portainer\n \033[0m")

os.system("docker run -ti --name portainer -p 127.0.0.1:9000:9000 --restart always -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer")

# MESSAGE
print("\033[36;1m \nLien vers portainer http://localhost:9000\n \033[0m")

entree = raw_input("\033[36;1m \nAppuyer sur <Entrée> for confirmer \033[0m")

if entree == "":
    pass
