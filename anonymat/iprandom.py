# coding:utf-8

'''
module pour l'installation d'un script d'ip aléatoire automatique
'''

print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git")

print("\033[36;1m \nMise en place du script\n \033[0m")

os.system("sudo mkdir $HOME/vpn")

print("\033[36;1m" "VOUS DEVEZ METTRE LES FICHIERS openvpn.conf DANS LE DOSSIER VPN POUR QUE LE SCRIPT FONCTIONNE\n" "\033[0m")

entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
    continue

os.system("git clone https://github.com/oda-alexandre/ip_random.git && \
sudo mv -f ip_random/ip-random /etc/init.d/ && \
sudo chmod +x /etc/init.d/ip-random && \
sudo update-rc.d -f ip-random defaults && \
rm -rf ip_random")

continue
