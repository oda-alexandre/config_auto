# coding:utf-8

'''
module pour l'installation de vim avec fichier de configuration personnaliser
'''

print("\033[36;1m \nUpdate\n \033[0m")

os.system("sudo apt-get update")

print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt install --no-install-recommends -y \
vim \
git")

print("\033[36;1m \nInstallation du fichier de configuration\n \033[0m")

os.system("git clone https://github.com/oda-alexandre/vimrc.git && \
sudo cp vimrc/vimrc /etc/vim/ && \
rm -rf vimrc")

continue
