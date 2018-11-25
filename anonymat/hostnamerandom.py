# coding:utf-8

'''
module pour l'installation d'un script de hostname aléatoire automatique
'''

print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git")

print("\033[36;1m \nMise en place du script\n \033[0m")

os.system("sudo mkdir /usr/share/wordlists && \
git clone https://github.com/oda-alexandre/hostname_random.git && \
sudo mv -f hostname_random/names.txt /usr/share/wordlist/ && \
sudo mv -f hostname_random/hostname-random /etc/init.d/ && \
sudo chmod +x /etc/init.d/hostname-random && \
sudo update-rc.d -f hostname-random defaults && \
rm -rf hostname_random")

continue
