# coding:utf-8

'''
module pour l'installation de tor et de privoxy
'''

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
tor \
privoxy")

# CONFIGURATION DU FICHIER /etc/privoxy/config
print("\033[36;1m \nConfiguration\n \033[0m")

os.system("echo \"forward-socks5 / localhost:9050 .\" | sudo tee -a /etc/privoxy/config && \
echo \"forward-socks4 / localhost:9050 .\" | sudo tee -a /etc/privoxy/config && \
echo \"forward-socks4a / localhost:9050 .\" | sudo tee -a /etc/privoxy/config")

# CONFIGURATION MANUELLE DU RESEAU
print("\033[36;1m"
      "AJOUTER CES LIGNES DANS PARAMETRE / RESEAU / SERVEUR MANDATAIRE / METHODE MANUELLE :\n\n"

      "HTTP localhost - 8118\n"
      "HTTPS localhost - 8118\n"
      "Socks localhost - 9050\n"
      "\n"
      "\033[0m")

entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
    continue

# DESACTIVATION DES INTERFACES RESEAUX
print("\033[36;1m \nDésactivation des interfaces réseaux\n \033[0m")

os.system("sudo ifconfig wlan0 down && \
sudo ifconfig eth0 down && \
sudo service network-manager stop")

# ACTIVATION DES SERVICES TOR & PRIVOXY
print("\033[36;1m \nActivation des services\n \033[0m")

os.system("sudo update-rc.d -f tor remove && \
sudo update-rc.d -f privoxy remove && \
sudo update-rc.d -f tor defaults && \
sudo update-rc.d -f privoxy defaults && \
sudo update-rc.d -f tor enable && \
sudo update-rc.d -f privoxy enable && \
")

# REACTIVATION DES INTERFACES RESEAUX
print("\033[36;1m \nRéactivation des interfaces réseaux\n \033[0m")

os.system("sudo ifconfig wlan0 up && \
sudo ifconfig eth0 up && \
sudo service network-manager start && \
sudo service privoxy start && \
sudo service tor start")

continue
