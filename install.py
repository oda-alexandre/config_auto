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
    print("\033[36;1m" "\nCe script ne fonctionne pas en root, un compte utilisateur va étre créé" "\033[36;1m")
    os.system("read -p 'Entrez votre nom : ' nom && \
    adduser $nom && \
    adduser $nom sudo && \
    su $nom")

###
# VERIF OS
###
if not platform.platform('kali'):
    sys.exit("\033[36;1m" "\nCe script ne fonctionne que sur une distribution Kali Linux" "\033[36;1m")

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

          " 1 Kali build             => Création d'une ISO minimaliste de kali avec configurateur automatisé\n"
          " 2 Sources.list           => Modification des sources.list & update/upgrade/dist-upgrade\n"
          " 3 Gnome mini             => Configuration minimaliste de gnome\n"
          " 4 Theme sombre           => Utiliser le theme sombre integrale\n"
          " 5 Bluetooth              => Activation du bluetooth\n"
          " 6 Son                    => Activation du son\n"
          " 7 Grub                   => Acceleration du temps de demarrage du grub et affichage des logs de boot\n"
          " 8 Grub fond d'ecran      => Modification du fond d'ecran du grub\n"
          " 9 Vimrc                  => Vim avec copier/coller & couleur syntax & souris\n"
          " 10 Terminal Custom        => Terminal personnaliser\n"
          " 11 Conky                 => Moniteur Systeme personnailer\n"
          " 12 Htop                  => Moniteur Systeme terminal\n"
          " 13 Auto clean            => Nettoyage a chaque demarrage\n"
          " 14 Auto Destruction      => (Pour OS installer en lvm chiffree) Mot de passe auto destruction\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "ANONYMAT\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 20 Hostname Random       => Change le nom de l'ordinateur a chaque demarrage\n"
          " 21 Mac Random            => Change les adresses mac a chaque demarrage\n"
          " 22 Noip                  => Synchronisation de l'ip public avec Noip toutes les minutes\n"
          " 23 Ip Random             => Change l'IP de l'ordinateur a chaque demarrage\n"
          " 24 Tor Privoxy           => Passe tout le trafic reseau a travers Tor Privoxy par connection mandataire\n"
          "\n"

          "------------------------------------------------------------------------------------------------------------------\n"
          "VIRTUALISATION\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 31 Virtualbox            => Programme de virtualisation\n"
          " 32 Docker                => Installation de docker avec interface graphique portainer\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "FIREWALL / IDS / DNS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 41 Snort                 => (docker) Detecteur d'intrusion\n"
          " 42 DnsCrypt              => en cours de dev (docker) Chiffrement dns\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "PENTEST\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 51 Armitage              => en cours de dev (docker) Integration de Beef-xss, Msf,Nmap,Geoip dans Armitage\n"
          " 52 Gophish               => (docker) Programme de phishing\n"
          " 53 OnionScan             => (docker) Scanner de site .onion\n"
          " 54 Ufonet                => (docker) Programme de Ddos\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "WEB\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 60 Pelican               => (docker) Generateur de site static\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "NAVIGATEURS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 70 Firefox               => (docker) Navigateur simple\n"
          " 71 Opera                 => (docker) Navigateur avec vpn\n"
          " 72 Tor Browser           => (docker) Navigateur du reseau tor\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "MESSAGERIES\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 80 Pidgin                => (docker) Messagerie instantanee .onion\n"
          " 81 Discord               => (docker) Plateforme Voip\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CLOUDS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 90 Dropbox               => (docker) Service Cloud\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CONTROLE DISTANT\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 100 Teamviewer            => (docker) Prise de controle a distance\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CHIFFREMENTS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 110 Keepassx              => (docker) Gestionnaire de mot de passe\n"
          " 111 PeaZip                => (docker) Gestionnaire d'archive (zip,rar...)\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "OUTILS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 120 Atom                  => (docker) Editeur de code\n"
          " 121 Libreoffice           => (docker) Suite bureautique\n"
          " 122 Obs                   => Capture & streaming video\n"
          " 123 OpenShot              => Editeur video\n"
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
# MODULES CONFIGURATION
###
        elif choixMenu == "1":
            import configuration.kalibuild

        elif choixMenu == "2":
            import configuration.sourceslist

        elif choixMenu == "3":
            import configuration.gnomemini

        elif choixMenu == "4":
            import configuration.themesombre

        elif choixMenu == "5":
            import configuration.bluetooth

        elif choixMenu == "6":
            import configuration.son

        elif choixMenu == "7":
            import configuration.grub

        elif choixMenu == "8":
            import configuration.grubimg

        elif choixMenu == "9":
            import configuration.vimrc

        elif choixMenu == "10":
            import configuration.terminalcustom

        elif choixMenu == "11":
            import configuration.conky

        elif choixMenu == "12":
            import configuration.htop

        elif choixMenu == "13":
            import configuration.autoclean

        elif choixMenu == "14":
            import configuration.autodestruction

###
# MODULES ANONYMAT
###
        elif choixMenu == "20":
            import anonymat.hostnamerandom

        elif choixMenu == "21":
            import anonymat.macrandom

        elif choixMenu == "22":
            import anonymat.noip

        elif choixMenu == "23":
            import anonymat.iprandom

        elif choixMenu == "24":
            import anonymat.torprivoxy

###
# MODULES VIRTUALISATION
###
        elif choixMenu == "30":
            import virtualisation.virtualbox

        elif choixMenu == "31":
            import virtualisation.docker

###
# MODULES FIREWALL
###
        elif choixMenu == "40":
            import firewall.snort

        elif choixMenu == "41":
            import firewall.dnscrypt

###
# MODULES PENTEST
###
        elif choixMenu == "50":
            import pentest.armitage

        elif choixMenu == "51":
            import pentest.gophish

        elif choixMenu == "52":
            import pentest.onionscan

        elif choixMenu == "53":
            import pentest.ufonet

###
# MODULES WEB
###
        elif choixMenu == "60":
            import web.pelican

###
# MODULES NAVIGATEURS
###
        elif choixMenu == "70":
            import navigateurs.firefox

        elif choixMenu == "71":
            import navigateurs.opera

        elif choixMenu == "72":
            import navigateurs.torbrowser

###
# MODULES MESSAGERIES
###
        elif choixMenu == "80":
            import messageries.pidgin

        elif choixMenu == "81":
            import messageries.discord

###
# MODULES CLOUDS
###
        elif choixMenu == "90":
            import clouds.dropbox

###
# MODULES CONTROLE DISTANT
###
        elif choixMenu == "100":
            import controledistant.teamviewer

###
# MODULES CHIFFREMENTS
###
        elif choixMenu == "110":
            import Chiffrements.keepassx

        elif choixMenu == "111":
            import Chiffrements.peazip


###
# MODULES OUTILS
###
        elif choixMenu == "120":
            import outils.atom

        elif choixMenu == "121":
            import outils.libreoffice

        elif choixMenu == "122":
            import outils.obs

        elif choixMenu == "123":
            import outils.openshot

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
