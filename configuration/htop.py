# coding:utf-8

'''
module pour l'installation de htop avec terminal xterm
'''

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
htop \
xterm")

continue
