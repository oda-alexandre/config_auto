# coding:utf-8

'''
module pour l'installation d'un script de syncronisation automatique de l'ip publique avec noip
'''

# INSTALLATION DES PREREQUIS
print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
git \
wget")

# INSTALLATION DE NOIP
print("\033[36;1m \nInstallation de noip\n \033[0m")

os.system("wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz -O && \
noip-duc-linux.tar.gz && \
sudo tar xf noip-duc-linux.tar.gz -C /usr/local/src/")

# MESSAGE
print("\033[36;1m"
      "\n"
      "DANS LA FENETRE QUI VAS SUIVRE RENSEIGNER COMME CECI :\n"

      "(POUR CREER UN COMPTE NOIP SUIVRE CE LIEN\n" "https://www.noip.com/sign-up)\n"
      "(POUR CREER VOTRE COMPTE VIA UNE EMAIL JETABLE SUIVRE CE LIEN\n" "https://www.crazymailing.com/fr/)\n"

      "1-Entrez votre email noip\n"
      "2-Entrez votre mot de passe noip\n"
      "3-Entrez y et renseignez le temps entre chaque syncronisation (default 30min)\n"
      "4-Entrez y Appuyez sur entrer\n"
      "\n"
      "\033[0m")

entree = input(
    "\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

# CONFIGURATION DE NOIP
os.system("sudo make install -C /usr/local/src/noip-*/")

print("\033[36;1m \nMise en place du script\n \033[0m")

# INSTALLATION DU SCRIPT /etc/init.d/noip
os.system("git clone https://github.com/oda-alexandre/noip.git noip && \
sudo mv -f noip/noip /etc/init.d/ && \
sudo chmod +x /etc/init.d/noip")

# NETTOYAGE DES RESIDUS D'INSTALLATION
os.system("rm -rf noip && \
rm -rf noip-duc-linux.tar.gz && \
sudo rm -rf /usr/local/src/noip-duc-linux.tar.gz")

# LANCEMENT DES SERVICES AU DEMARRAGE
os.system("sudo update-rc.d -f noip defaults && \
sudo service noip start && \
noip2 -U 1")

# MESSAGE
print("\033[36;1m"
      "\n"
      "POUR VERIFIER LE STATUS TAPER DANS UN TERMINAL :\n\n"

      "noip2 -S"
      "\n"
      "\033[0m")

entree = input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
