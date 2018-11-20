# coding:utf-8

"""
Maintainer:  https://oda-alexandre.github.io
Description: Configurateur automatisé pour Kali Linux
Prerequis:   Python
Tutoriel:    https://www.youtube.com/channel/UCELtTOkvfaLoZzUWZ6zywJQ
"""

###
# IMPORT
###
import os
import sys
import platform

###
# VERIF USER
###
if os.geteuid() == 0:
    sys.exit("\033[36;1m" "\nCe script ne fonctionne pas en root" "\033[36;1m")

###
# VERIF OS
###
if not platform.platform('kali'):
    sys.exit(
        "\033[36;1m" "\nCe script ne fonctionne que sur une distribution Kali Linux" "\033[36;1m")

###
# MENU
###
programmeLancer = True

while programmeLancer:

    print("\033[36;1m"
          "\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "CONFIGURATION\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 1 Sources.list           => Modification des sources.list & update/upgrade/dist-upgrade\n"
          " 2 Gnome mini             => Configuration minimaliste de gnome\n"
          " 3 Theme sombre           => Utiliser le theme sombre integrale\n"
          " 4 Bluetooth              => Activation du bluetooth\n"
          " 5 Son                    => Activation du son\n"
          " 6 Grub                   => Acceleration du temps de demarrage du grub et affichage des logs de boot\n"
          " 7 Grub fond d'ecran      => Modification du fond d'ecran du grub\n"
          " 8 Vimrc                  => Vim avec copier/coller & couleur syntax & souris\n"
          " 9 Terminal Custom        => Terminal personnaliser\n"
          " 10 Conky                 => Moniteur Systeme personnailer\n"
          " 11 Htop                  => Moniteur Systeme terminal\n"
          " 12 Auto clean            => Nettoyage a chaque demarrage\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "ANONYMAT\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 13 Hostname Random       => Change le nom de l'ordinateur a chaque demarrage\n"
          " 14 Mac Random            => (Indisponnible sur VirtualBox) Change les adresses mac a chaque demarrage\n"
          " 15 Noip                  => Synchronisation de l'ip public avec Noip toutes les minutes\n"
          " 16 Ip Jetable            => Installation vpn pptp & configuration de ip jetable\n"
          " 17 Tor Privoxy           => Passe tout le trafic reseau a travers Tor Privoxy par connection mandataire\n"
          " 18 Auto Destruction      => (Pour OS installer en lvm chiffree) Mot de passe auto destruction\n"
          "\n"

          "------------------------------------------------------------------------------------------------------------------\n"
          "VIRTUALISATION\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 19 Virtualbox            => Programme de virtualisation\n"
          " 20 Docker                => Installation de docker avec interface graphique portainer\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "FIREWALL / IDS / DNS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 21 Snort                 => (docker) Detecteur d'intrusion\n"
          " 22 DnsCrypt              => en cours de dev (docker) Chiffrement dns\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "PROGRAMME WEB\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 23 Armitage              => en cours de dev (docker) Integration de Beef-xss, Msf,Nmap,Geoip dans Armitage\n"
          " 24 Gophish               => (docker) Programme de phishing\n"
          " 25 OnionScan             => (docker) Scanner de site .onion\n"
          " 26 Ufonet                => (docker) Programme de Ddos\n"
          " 27 Pelican               => (docker) Generateur de site static\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "NAVIGATEUR\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 28 Firefox               => (docker) Navigateur simple\n"
          " 29 Opera                 => (docker) Navigateur avec vpn\n"
          " 30 Tor Browser           => (docker) Navigateur du reseau tor\n"
          " 31 Owasp Mantra          => en cours de dev (docker) Navigateur de pentest\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "MESSAGERIE\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 32 Pidgin                => (docker) Messagerie instantanee .onion\n"
          " 33 Discord               => (docker) Plateforme Voip\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CLOUD\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 34 Dropbox               => (docker) Service Cloud\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "ACCES A DISTANCE\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 35 Teamviewer            => (docker) Prise de controle a distance\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CHIFFREMENTS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 36 Keepassx              => (docker) Gestionnaire de mot de passe\n"
          " 37 PeaZip                => (docker) Gestionnaire d'archive (zip,rar...)\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "OUTILS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 38 Atom                  => (docker) Editeur de code\n"
          " 39 Libreoffice           => (docker) Suite bureautique\n"
          " 40 Vokoscreen            => Capture video\n"
          " 41 OpenShot              => Editeur video\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "OPTIONS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 0 Quitter                => Quitter le programme d'installation\n"
          "\n"
          "\033[36;1m")

###
# CHOIX MENU
###
    try:
        choixMenu = raw_input(
            "\033[36;1m" "VEUILLEZ SAISIR VOTRE CHOIX : " "\033[36;1m")
        choixMenu = str(choixMenu)

###
# QUITTER
###
        if choixMenu == "0":
            print("\033[36;1m" "\nMerci aurevoir\n" "\033[36;1m")
            programmeLancer = False


###
# SOURCES.LIST
###
        elif choixMenu == "1":

            print("\033[36;1m \nModification du fichier sources.list...\n \033[0m")

            os.system("sudo rm -f /etc/apt/sources.list")

            os.system("echo \"deb https://http.kali.org/kali kali-rolling main contrib non-free\" | sudo tee -a /etc/apt/sources.list")

            os.system("echo \"deb-src https://http.kali.org/kali kali-rolling main contrib non-free\" | sudo tee -a /etc/apt/sources.list")

            print("\033[36;1m \nupdate...\n \033[0m")

            os.system("sudo apt update")

            print("\033[36;1m \nupgrade...\n \033[0m")

            os.system("sudo apt upgrade -y")

            print("\033[36;1m \ndist-upgrade...\n \033[0m")

            os.system("sudo apt dist-upgrade -y")

            print("\033[36;1m \n--purge autoremove & autoclean...\n \033[0m")

            os.system("sudo apt-get --purge autoremove -y && sudo apt-get autoclean -y")

            print("\033[36;1m \nAjout alias maj dans le .bashrc\n \033[0m")

            os.system("echo \"alias maj=\'sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y && sudo apt-get --purge autoremove -y && sudo apt-get autoclean -y\'\" >> $HOME/.bashrc")

            continue

###
# GNOME-MINI
###
        elif choixMenu == "2":

            print("\033[36;1m \nInstallation des prérequis...\n \033[0m")

            os.system("sudo apt install --no-install-recommends -y gdm3 gnome-theme-kali gnome-session gnome-control-center gnome-tweaks gnome-terminal network-manager-gnome nautilus nautilus-extension-gnome-terminal gnome-icon-theme gnome-disk-utility gnome-shell-extensions xserver-xorg xfonts-base kali-defaults kali-desktop-live desktop-base kali-root-login sudo bash-completion net-tools")

            print("\033[36;1m \nSuppression des paquets inutiles...\n \033[0m")

            os.system("sudo apt-get --purge autoremove -y chromium* chrome* firefox-esr leafpad xpdf cherrytree evince tracker gnome-online-miners gnome-online-accounts gnome-orca gnome-characters gnome-contacts gnome-shell-extension-easyscreencast gnome-system-monitor gnome-user-docs gnome-font-viewer gnome-software-common python3-software-properties baobab florence gedit file-roller gnome-logs zim yelp reportbug eog vim-gui-common vim-common vim-tiny")

            print("\033[36;1m \nDesactivation des services inutiles...\n \033[0m")

            os.system("sudo mv /usr/lib/evolution/ /usr/lib/evolution-DISABLE/")

            os.system("sudo mv /usr/lib/evolution-data-server/ /usr/lib/evolution-data-server-DISABLE/")

            print("\033[36;1m \nSuppression des dossiers inutiles...\n \033[0m")

            os.system("rm -rf $HOME/Modèles $HOME/Musique $HOME/Public $HOME/Téléchargements $HOME/Vidéos $HOME/Documents $HOME/Images")

            os.system("sudo rm -rf /root/Modèles /root/Musique /root/Public /root/Téléchargements /root/Vidéos /root/Documents /root/Images")

            continue

###
# THEME-SOMBRE
###
        elif choixMenu == "3":

            print("\033[36;1m \nConfiguration theme sombre...\n \033[0m")

            os.system("echo '[Settings]' >> $HOME/.config/gtk-3.0/settings.ini")

            os.system("echo 'gtk-application-prefer-dark-theme=1' >> $HOME/.config/gtk-3.0/settings.ini")

            continue

###
# BLUETOOTH
###
        elif choixMenu == "4":

            print("\033[36;1m \nActivation du bluetooth...\n \033[0m")

            os.system("sudo apt update")

            os.system("sudo apt install --no-install-recommends -y bluetooth")

            os.system("sudo systemctl enable bluetooth.service")

            os.system("sudo systemctl start bluetooth.service")

            continue

###
# SON
###
        elif choixMenu == "5":

            print("\033[36;1m \nActivation du son...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y pulseaudio")

            continue

###
# GRUB
###
        elif choixMenu == "6":

            print("\033[36;1m \nModification timeout grub...\n \033[0m")

            os.system("sudo sed -i 's/GRUB_TIMEOUT=5/GRUB_TIMEOUT=1/g' /etc/default/grub")

            os.system("sudo sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT=\"quiet\"/#GRUB_CMDLINE_LINUX_DEFAULT=\"quiet\"/g' /etc/default/grub")

            print("\033[36;1m \nupdate grub...\n \033[0m")

            os.system("sudo update-grub")

            continue

###
# GRUB FOND D'ECRAN
###
        elif choixMenu == "7":

            print("\033[36;1m \nModification arriere plan du grub...\n \033[0m")

            print("\033[36;1m \nPlacez votre image background_cache.png dans votre dossier personnel\n \033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                pass
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
                continue

            os.system("sudo rm -f /boot/grub/.background_cache.png")

            os.system("sudo cp $HOME/background_cache.png /boot/grub/background_cache.png")

            os.system("sudo update-grub")

            continue

###
# VIMRC
###
        elif choixMenu == "8":

            print("\033[36;1m \nMise en place du fichier de configuration...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y vim git")

            os.system("git clone https://github.com/oda-alexandre/vimrc.git")

            os.system("sudo cp vimrc/vimrc /etc/vim/")

            print("\033[36;1m \nSuppression des residus de configuration...\n \033[0m")

            os.system("rm -rf vimrc")

            continue

###
# TERMINAL-CUSTOM
###
        elif choixMenu == "9":

            print("\033[36;1m \nInstallation de terminator...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y terminator")

            print("\033[36;1m \nMise en place du script .bashrc...\n \033[0m")

            os.system("git clone https://github.com/oda-alexandre/terminal-custom.git")

            os.system("cp terminal_custom/bashrc $HOME/.bashrc")

            os.system("sudo cp terminal_custom/bashrc /root/.bashrc")

            print("\033[36;1m \nSuppression des residus de configuration...\n \033[0m")

            os.system("rm -rf terminal_custom")

            continue

###
# CONKY
###
        elif choixMenu == "10":

            print("\033[36;1m \nInstallation de conky...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommands -y psmisc conky-manager")

            os.system("mkdir $HOME/.conky")

            print("\033[36;1m \nMise en place du conky...\n \033[0m")

            os.system("sudo apt install --no-install-recommends -y git")

            os.system("git clone https://github.com/oda-alexandre/conky.git")

            os.system("sudo mv conky/conky/pizzadude_bullets /usr/share/fonts")

            os.system("cp -r conky/conky $HOME/.conky")

            os.system("rm -rf conky")

            print("\033[36;1m \nDANS LA FENETRE QUI VAS S'OUVRIR SELECTIONNER VOTRE CONKY\n \033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                pass
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
                continue

            os.system("conky-manager")

            continue

###
# HTOP
###
        elif choixMenu == "11":

            print("\033[36;1m \nInstallation de Htop...\n \033[0m")

            os.system("sudo apt install --no-install-recommends -y htop xterm")

            continue

###
# MAC RANDOM
###
        elif choixMenu == "14":

            print("\033[36;1m \nMise en place du script mac_random...\n \033[0m")

            os.system("sudo apt install --no-install-recommends -y git")

            os.system("git clone https://github.com/oda-alexandre/mac_random.git")

            os.system("sudo mv -f mac_random/mac-random /etc/init.d/")

            os.system("sudo chmod +x /etc/init.d/mac-random")

            print("\033[36;1m \nMise en place demarrage auto...\n \033[0m")

            os.system("sudo update-rc.d -f mac-random defaults")

            print("\033[36;1m \nSuppression des residus de configuration...\n \033[0m")

            os.system("rm -rf mac_random")

            continue

###
# HOSTNAME RANDOM
###
        elif choixMenu == "13":

            print("\033[36;1m \nMise en place du script hostname_random...\n \033[0m")

            os.system("sudo mkdir /usr/share/wordlists")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y git")

            os.system("git clone https://github.com/oda-alexandre/hostname_random.git")

            os.system("sudo mv -f hostname_random/names.txt /usr/share/wordlist/")

            os.system("sudo mv -f hostname_random/hostname-random /etc/init.d/")

            os.system("sudo chmod +x /etc/init.d/hostname-random")

            print("\033[36;1m \nMise en place demarrage auto...\n \033[0m")

            os.system("sudo update-rc.d -f hostname-random defaults")

            print("\033[36;1m \nSuppression des residus de configuration...\n \033[0m")

            os.system("rm -rf hostname_random")

            continue

###
# AUTO CLEAN
###
        elif choixMenu == "12":

            print("\033[36;1m \nMise en place du script auto_clean...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y git")

            os.system("git clone https://github.com/oda-alexandre/auto_clean.git")

            os.system("sudo mv -f auto_clean/auto-clean /etc/init.d/")

            os.system("sudo chmod +x /etc/init.d/auto-clean")

            print("\033[36;1m \nMise en place demarrage auto...\n \033[0m")

            os.system("sudo update-rc.d -f auto-clean defaults")

            print("\033[36;1m \nSuppression des residus de configuration...\n \033[0m")

            os.system("rm -rf auto_clean")

            continue

###
# NOIP
###
        elif choixMenu == "15":

            print("\033[36;1m \nInstallation de noip...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y wget")

            os.system("wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz -O")

            os.system("noip-duc-linux.tar.gz")

            os.system("sudo tar xf noip-duc-linux.tar.gz -C /usr/local/src/")

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

            entree = raw_input(
                "\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                pass
            else:
                print(
                    "\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
                continue

            os.system("sudo make install -C /usr/local/src/noip-*/")

            print("\033[36;1m \nMise en place du script noip...\n \033[0m")

            os.system("sudo apt install --no-install-recommends -y git")

            os.system("git clone https://github.com/oda-alexandre/noip.git noip")

            os.system("sudo mv -f noip/noip /etc/init.d/")

            os.system("sudo chmod +x /etc/init.d/noip")

            os.system("sudo update-rc.d -f noip defaults")

            print("\033[36;1m \nAjout alias maj dans le .bashrc\n \033[0m")

            os.system("echo \"alias noip-restart=\'sudo service noip restart\'\" >> $HOME/.bashrc")

            print("\033[36;1m \nSuppression des residus de configuration...\n \033[0m")

            os.system("rm -rf noip")

            os.system("rm -rf noip-duc-linux.tar.gz")

            os.system("sudo rm -rf /usr/local/src/noip-duc-linux.tar.gz")

            print("\033[36;1m \nReglage du temps de synchronisation noip sur 1 min...\n \033[0m")

            os.system("sudo service noip start")

            os.system("noip2 -U 1")

            print("\033[36;1m"
                  "\n"
                  "POUR VERIFIER LE STATUS TAPER DANS UN TERMINAL :\n\n"

                  "noip2 -S"
                  "\n"
                  "\033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                continue
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

                continue

###
# IP JETABLE
###
        elif choixMenu == "16":

            print("\033[36;1m \nInstallation de pptp...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y network-manager-pptp-gnome")

            print("\033[36;1m"
                  "\n"
                  "POUR CREER UN COMPTE IP JETABLE SUIVRE CE LIEN\n" "https://ipjetable.net/\n\n"

                  "BENEFICIER D'UN MOIS GRATUIT AVEC LE CODE FCZKCXSNKDHEQVLA\n\n"

                  "POUR CREER VOTRE COMPTE VIA UNE EMAIL JETABLE SUIVRE CE LIEN\n" "https://www.crazymailing.com/fr/\n\n"

                  "ALLER DANS PARAMETRE / RESEAU / VPN / AJOUTER PPTP ET RENTRER COMME CECI :\n\n"

                  "Nom               = au choix\n"
                  "Passerelle        = pptp.ipjetable.net\n"
                  "Nom d'utilisateur = fournis dans le mail ipjetable\n"
                  "Mot de passe      = fournis dans le mail ipjetable\n"
                  "Domaine           = laisser vide\n\n"

                  "ALLER DANS AVANCE ET COCHER :\n\n"

                  "Utiliser le chiffrement point-to-point (MPPE)\n"
                  "\n"
                  "\033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                continue
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
                continue

###
# TOR PRIVOXY
###
        elif choixMenu == "17":

            print("\033[36;1m \nInstallation de tor et privoxy...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y tor privoxy")

            print("\033[36;1m \nConfiguration socks...\n \033[0m")

            os.system("echo \"forward-socks5 / localhost:9050 .\" | sudo tee -a /etc/privoxy/config")

            os.system("echo \"forward-socks4 / localhost:9050 .\" | sudo tee -a /etc/privoxy/config")

            os.system("echo \"forward-socks4a / localhost:9050 .\" | sudo tee -a /etc/privoxy/config")

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

            print("\033[36;1m \nMise en place demarrage auto...\n \033[0m")

            os.system("sudo ifconfig wlan0 down")

            os.system("sudo ifconfig eth0 down")

            os.system("sudo service network-manager stop")

            os.system("sudo update-rc.d -f tor remove")

            os.system("sudo update-rc.d -f privoxy remove")

            os.system("sudo update-rc.d -f tor defaults")

            os.system("sudo update-rc.d -f privoxy defaults")

            os.system("sudo update-rc.d -f tor enable")

            os.system("sudo update-rc.d -f privoxy enable")

            os.system("sudo ifconfig wlan0 up")

            os.system("sudo ifconfig eth0 up")

            os.system("sudo service network-manager start")

            os.system("sudo service privoxy start")

            os.system("sudo service tor start")

            continue

###
# MOT DE PASSE AUTO DESTRUCTION POUR LVM CHIFFREE
###
        elif choixMenu == "18":

            print("\033[36;1m"
                  "\n"
                  "DANS LA FENETRE QUI VAS SUIVRE RENSEIGNER COMME CECI :\n\n"

                  "1-Entrez votre mot de passe de decryptage (celui utiliser au demarrage du PC)\n"
                  "2-Entrez votre mot de passe pour l'auto destruction\n"
                  "3-Comfirmer le mot de passe pour l'auto destruction\n"
                  "\n"
                  "\033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                pass
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
                continue

            os.system("sudo cryptsetup luksAddNuke /dev/sda3")

            continue

###
# VIRTUALBOX
###
        elif choixMenu == "19":

            print("\033[36;1m \nInstallation de virtualbox...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install -y virtualbox")

            os.system("sudo usermod -a -G vboxusers $USER")

            continue

###
# DOCKER
###
        elif choixMenu == "20":

            print("\033[36;1m \nInstallation de Docker...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt-get --purge autoremove -y docker*")

            os.system("sudo apt install --no-install-recommends -y gnupg2 apt-transport-https ca-certificates curl software-properties-common dirmngr")

            os.system("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -")

            os.system("echo \'deb https://download.docker.com/linux/debian stretch stable\' | sudo tee -a /etc/apt/sources.list.d/docker.list")

            os.system("sudo apt-get update")

            os.system("echo \'DOCKER_OPTS=\"-icc=false\"\' | sudo tee -a /etc/default/docker")

            os.system("sudo apt install --no-install-recommends -y docker-compose docker-ce docker docker.io")

            os.system("sudo systemctl start docker.service")

            os.system("sudo systemctl enable docker.service")

            os.system("sudo groupadd -f docker")

            os.system("sudo chown root:docker /var/run/docker.sock")

            os.system("sudo usermod -a -G docker $USER")

            os.system("newgrp docker")

            os.system("sudo systemctl restart docker.service")

            print("\033[36;1m \ninstallation de portainer...\n \033[0m")

            os.system("docker run -d --name portainer -p 127.0.0.1:9000:9000 --restart always -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer")

            print("\033[36;1m \nLien vers portainer http://localhost:9000\n \033[0m")

            entree = raw_input("\033[36;1m \nAppuyer sur <Entrée> pour confirmer \033[0m")

            if entree == "":

                continue

###
# SNORT
###
        elif choixMenu == "21":

            print("\033[36;1m \nEn cours de dev\n \033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                continue
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

                continue

###
# DNSCRYPT
###
        elif choixMenu == "22":

            print("\033[36;1m \nEn cours de dev\n \033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                continue
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

                continue

###
# ARMITAGE
###
        elif choixMenu == "23":

            print("\033[36;1m \nEn cours de dev\n \033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                continue
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

                continue


###
# GOPHISH
###
        elif choixMenu == "24":

            print("\033[36;1m \nInstallation de Gophish...\n \033[0m")

            os.system("docker run -d --name gophish -p 127.0.0.1:3333:3333 -p 80:80 alexandreoda/gophish")

            print("\033[36;1m \nlien vers Gophish https://127.0.0.1:3333/login (ID = admin / PASSWORD = gophish)\n \033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                continue
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

                continue

###
# ONIONSCAN
###
        elif choixMenu == "25":

            print("\033[36;1m \nInstallation de onionscan...\n \033[0m")

            os.system("docker run -ti --name onionscan alexandreoda/onionscan /bin/bash")

            os.system("echo \"alias onionscan=\'docker start onionscan && docker exec -ti onionscan /bin/bash\'\" >> $HOME/.bashrc")

            continue

###
# UFONET
###
        elif choixMenu == "26":

            print("\033[36;1m \nInstallation de ufonet...\n \033[0m")

            os.system("docker run -d --name ufonet -p 9999:9999 -e DISPLAY alexandreoda/ufonet")

            print("\033[36;1m \nlien vers Ufonet http://0.0.0.0:9999\n \033[0m")

            entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                continue
            else:
                print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

                continue

###
# PELICAN
###
        elif choixMenu == "27":

            print("\033[36;1m \nInstallation de pelican...\n \033[0m")

            os.system("docker run --name pelican -p 127.0.0.1:8000:8000  alexandreoda/pelican")

            continue

###
# FIREFOX
###
        elif choixMenu == "28":

            print("\033[36;1m \nInstallation de firefox...\n \033[0m")

            os.system("docker run -d --name firefox -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) -v ${HOME}:/home/firefox -e DISPLAY --network host alexandreoda/firefox")

            continue


###
# OPERA
###
        elif choixMenu == "29":

            print("\033[36;1m \nInstallation de opera...\n \033[0m")

            os.system("docker run -d --name opera -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) -v ${HOME}:/home/opera -e DISPLAY --network host alexandreoda/opera")

            continue

###
# TOR BROWSER
###
        elif choixMenu == "30":

            print("\033[36;1m \nInstallation de tor browser...\n \033[0m")

            os.system("docker run -d --name tor-browser -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) -v ${HOME}/tor-browser:/home/torbrowser -e DISPLAY --network host alexandreoda/tor-browser")

            continue

###
# OWASP-MANTRA
###
        elif choixMenu == "31":

            print("\033[36;1m \nInstallation de owasp-mantra...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y owasp-mantra-ff")

            continue

###
# PIDGIN
###
        elif choixMenu == "32":

            print("\033[36;1m \nInstallations de pidgin...\n \033[0m")

            os.system("docker run -d --name pidgin -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/pidgin -e DISPLAY alexandreoda/pidgin")

            print("\033[36;1m"
                  "\nCONFIGURER COMME CECI :\n"
                  "(Pour creer un compte XMPP en .onion via tor-browser suivre ce lien libertygb2nyeyay.onion:5280/register_web)\n"

                  "\n1- DANS PIDGIN / OUTILS / PREFERENCES / PROXY :\n"

                  "\n(cocher) utiliser une DNS avec SOCKS4\n"

                  "\nType de proxy	: Tor/Privacy (SOCKS5)\n"
                  "\nHote		: 127.0.0.1         Port            : 9050\n"
                  "Utilisateur	: laisser vide	Mot de passe	: laisser vide\n"

                  "\nACCEPTER LE CERTIFICAT\n"

                  "\n2- DANS PIDGIN / OUTILS / PLUGINS :\n"

                  "\n(cocher) Messagerie Confidentielle Off te Record\n"

                  "\n3- CHOISIR CONFIGURER LE PLUGIN (a coter de fermer)\n"

                  "\n(cliquer) sur produire\n"
                  "(cocher) Exiger messagerie privee\n"

                  "\nDANS VOS CONVERSATIONS CLIQUER SUR NON-PRIVE / NON-VERIFIER / AUTHENTIFIER LE CONTACT (votre interlocuteur devras faire pareil de son cote)\n"
                  "\033[0m")

            entree = raw_input(
                "\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

            if entree == "":
                continue
            else:
                print(
                    "\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

                continue

###
# DISCORD
###
        elif choixMenu == "33":

            print("\033[36;1m \nInstallation de discord...\n \033[0m")

            os.system("docker run -d --name discord -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/snd:/dev/snd -v /dev/shm:/dev/shm -v /var/run/dbus:/var/run/dbus -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native --group-add $(getent group audio | cut -d: -f3) -v ${HOME}:/home/discord -e DISPLAY alexandreoda/discord")

            continue

###
# DROPBOX
###
        elif choixMenu == "34":

            print("\033[36;1m \nInstallation de dropbox...\n \033[0m")

            os.system("docker run -d --name dropbox -v ${HOME}:/home/dropbox --restart=always alexandreoda/dropbox")

            os.system("echo \"alias dropbox=\'docker exec -ti dropbox /bin/bash\'\" >> $HOME/.bashrc")

            continue

###
# TEAMVIEWER
###
        elif choixMenu == "35":

            print("\033[36;1m \nInstallation de teamviewer...\n \033[0m")

            os.system("docker run -d --name teamviewer -e DISPLAY -e XAUTHORITY=${XAUTHORITY} -v /tmp/.X11-unix:/tmp/.X11-unix hurricane/teamviewer")

            continue

###
# KEEPASSX
###
        elif choixMenu == "36":

            print("\033[36;1m \nInstallation de keepassx...\n \033[0m")

            os.system("docker run -it --name keepassx --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/keepassx -e DISPLAY -v ${XAUTHORITY}:/xauthority:ro -e XAUTHORITY='/xauthority' --network none alexandreoda/keepassx")

            continue

###
# PEAZIP
###
        elif choixMenu == "37":

            print("\033[36;1m \nInstallation de PeaZip...\n \033[0m")

            os.system("docker run -d --name peazip -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/peazip -e DISPLAY --network none alexandreoda/peazip")

            continue

###
# ATOM
###
        elif choixMenu == "38":

            print("\033[36;1m \nInstallation de atom...\n \033[0m")

            os.system("docker run -d --name atom -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/atom -e DISPLAY alexandreoda/atom")

            continue

###
# LIBREOFFICE
###
        elif choixMenu == "39":

            print("\033[36;1m \nInstallation de libreoffice...\n \033[0m")

            os.system("docker run -d --name libreoffice -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/libreoffice -e DISPLAY --network none alexandreoda/libreoffice")

            continue

###
# VOKOSCREEN
###
        elif choixMenu == "40":

            print("\033[36;1m \nInstallation de vokoscreen...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y vokoscreen")

            continue

###
# OPENSHOT
###
        elif choixMenu == "41":

            print("\033[36;1m \nInstallation de openshot...\n \033[0m")

            os.system("sudo apt-get update")

            os.system("sudo apt install --no-install-recommends -y openshot")

            continue

###
# GESTION ERREUR
###
        else:
            print("\033[36;1m" "\nCe choix n'est pas dans la liste\n" "\033[36;1m")
            continue

    except KeyboardInterrupt:
        print("\033[36;1m" "\n\nMerci aurevoir\n" "\033[36;1m")
        programmeLancer = False

    except:
        print("\033[36;1m" "\nVous devez saisir un nombre\n" "\033[36;1m")
        continue
