# coding:utf-8

'''
module pour l'installation d'un script de nettoyage automatique
'''

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git")

# INSTALLATION DU SCRIPT /etc/init.d/auto-clean
print("\033[36;1m \nInstallation du script\n \033[0m")

os.system("git clone https://github.com/oda-alexandre/auto_clean.git && \
sudo mv -f auto_clean/auto-clean /etc/init.d/ && \
sudo chmod +x /etc/init.d/auto-clean")

# LANCEMENT DU SERVICE AU DEMARRAGE
os.system("sudo update-rc.d -f auto-clean defaults")

# NETTOYAGE DES RESIDUS D'INSTALLATION
os.system("rm -rf auto_clean")

continue
