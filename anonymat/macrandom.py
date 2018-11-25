# coding:utf-8

'''
module pour l'installation d'un script de mac aléatoire automatique
'''

print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt install --no-install-recommends -y \
git")

print("\033[36;1m \nMise en place du script\n \033[0m")

os.system("git clone https://github.com/oda-alexandre/mac_random.git && \
sudo mv -f mac_random/mac-random /etc/init.d/ && \
sudo chmod +x /etc/init.d/mac-random && \
sudo update-rc.d -f mac-random defaults && \
rm -rf mac_random")

continue
