# coding:utf-8

'''
module pour l'installation d'un script de nettoyage automatique
'''

print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git")

print("\033[36;1m \nInstallation du script\n \033[0m")

os.system("git clone https://github.com/oda-alexandre/auto_clean.git && \
sudo mv -f auto_clean/auto-clean /etc/init.d/ && \
sudo chmod +x /etc/init.d/auto-clean && \
sudo update-rc.d -f auto-clean defaults && \
rm -rf auto_clean")

continue
