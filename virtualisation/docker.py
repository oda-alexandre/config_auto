# coding:utf-8

'''
module pour l'installation de docker
'''

import os

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
gnupg2 \
apt-transport-https \
ca-certificates \
curl \
software-properties-common \
dirmngr")

# AJOUT DU REPOS ET DE LA CLEF GPG
print("\033[36;1m \nAjout du repos et de la clef gpg\n \033[0m")

os.system("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add - && \
echo \'deb https://download.docker.com/linux/debian stretch stable\' | sudo tee -a /etc/apt/sources.list.d/docker.list")

# INSTALLATION DE DOCKER
print("\033[36;1m \nInstallation de docker\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
docker.ce")

# ACTIVATION DU SERVICE
print("\033[36;1m \nActivation du service\n \033[0m")

os.system("sudo systemctl start docker.service && \
sudo systemctl enable docker.service")

# CREATION DU GROUPE DOCKER
print("\033[36;1m \nCréation du groupe docker\n \033[0m")

os.system("sudo groupadd -f docker")

# SECURISATION DES DROITS SOCK
print("\033[36;1m \nSécurisation des droits sock\n \033[0m")

os.system("sudo chown root:docker /var/run/docker.sock")

# AJOUT DE L'UTILISATEUR AU GROUPE DOCKER
print("\033[36;1m \nAjout de l'utilisateur au groupe docker\n \033[0m")

os.system("sudo usermod -a -G docker $USER && \
newgrp docker")

# SECURISATIONS DES COMMUNICATIONS INTER CONTENEURS
print("\033[36;1m \nIsolation des communications inter-conteneurs\n \033[0m")

os.system("echo \'DOCKER_OPTS=\"-icc=false\"\' | sudo tee -a /etc/default/docker")

# REDEMARRAGE DU SERVICE DOCKER
print("\033[36;1m \nRedémarrage du service\n \033[0m")

os.system("sudo systemctl restart docker.service")

# INSTALLATION DE L'INTERFACE GRAPHIQUE PORTAINER DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation du gestionnaire portainer\n \033[0m")

os.system("docker run -ti --name portainer -p 127.0.0.1:9000:9000 --restart always -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer")

# MESSAGE
print("\033[36;1m \nLien vers portainer http://localhost:9000\n \033[0m")

entree = raw_input("\033[36;1m \nAppuyer sur <Entrée> pour confirmer \033[0m")

if entree == "":
    pass
