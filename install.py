# coding:utf-8

"""
Maintainer:  https://oda-alexandre.github.io
Description: Configurateur automatisé pour Kali Linux
Prerequis:   Python
Tutoriel:    https://www.youtube.com/channel/UCELtTOkvfaLoZzUWZ6zywJQ
"""

# IMPORTATION DES MODULES PYTHON
import os
import sys
import platform

# VERIFICATION DE L'UTILISATEUR EN COURS
if os.geteuid() == 0:

# CREATION D'UN UTILISATEUR EN CAS D'UTILISATION DU COMPTE ROOT
    print("\033[36;1m" "\nCe script ne fonctionne pas en root, un compte utilisateur va étre créé" "\033[36;1m")

    os.system("read -p 'Entrez votre nom : ' nom && \
    adduser $nom && \
    adduser $nom sudo && \
    su $nom")

# DEPLACEMENT DU PROGRAMME EN COURS VERS LE DOSSIER PERSONNEL DU NOUVEL UTILISATEUR
    os.system("sudo mv /root/config_auto $HOME/ && \
    python config_auto/install.py")

# VERIFICATION DE L'OS EN COURS
if not platform.platform('kali'):
    sys.exit("\033[36;1m" "\nCe script ne fonctionne que sur une distribution Kali Linux" "\033[36;1m")

# MENU
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
          " 10 Terminal Custom       => Terminal personnaliser\n"
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
          " 22 Ip Random             => Change l'IP de l'ordinateur a chaque demarrage\n"
          " 23 Tor Privoxy           => Passe tout le trafic reseau a travers Tor Privoxy par connection mandataire\n"
          "\n"

          "------------------------------------------------------------------------------------------------------------------\n"
          "VIRTUALISATION\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 30 Virtualbox            => Programme de virtualisation\n"
          " 31 Docker                => Installation de docker avec interface graphique portainer\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "FIREWALL / IDS / DNS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 40 Snort                 => (docker) Detecteur d'intrusion\n"
          " 41 DnsCrypt              => en cours de dev (docker) Chiffrement dns\n"
          " 42 Noip                  => Synchronisation de l'ip public avec Noip toutes les minutes\n"

          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "PENTEST\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 50 Armitage              => en cours de dev (docker) Beef-xss, Msf,Nmap,Geoip via Armitage\n"
          " 51 Gophish               => (docker) Programme de phishing\n"
          " 52 OnionScan             => (docker) Scanner de site .onion\n"
          " 53 Ufonet                => (docker) Programme de Ddos\n"
          " 54 Cupp                  => (docker) Gestion & creation de wordlists\n"
          " 55 WebShell              => Bibliotheque webshell\n"
          " 56 Sqlmap                => (docker) Programme d'injection sql\n"
          " 57 Maltego               => (docker) Programme de footprinting\n"
          " 58 Wifite                => (docker) Programme de crack wifi\n"
          " 59 Nikto                 => (docker) Scanner de serveur web\n"
          " 60 Whatweb               => (docker) Scanner de site web\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CMS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 70 Pelican               => (docker) Generateur de site static\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "NAVIGATEURS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 80 Firefox               => (docker) Navigateur simple\n"
          " 81 Opera                 => (docker) Navigateur avec vpn\n"
          " 82 Tor Browser           => (docker) Navigateur du reseau tor\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "MESSAGERIES\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 90 Pidgin                => (docker) Messagerie instantanee .onion\n"
          " 91 Discord               => (docker) Plateforme Voip\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CLOUDS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 100 Dropbox               => (docker) Service Cloud\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CONTROLE DISTANT\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 110 Teamviewer           => (docker) Prise de controle a distance\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CHIFFREMENTS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 120 Keepassx             => (docker) Gestionnaire de mot de passe\n"
          " 121 PeaZip               => (docker) Gestionnaire d'archive (zip,rar...)\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "OUTILS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 130 Atom                 => (docker) Editeur de code\n"
          " 131 Libreoffice          => (docker) Suite bureautique\n"
          " 132 Obs                  => Capture & streaming video\n"
          " 133 OpenShot             => Editeur video\n"
          " 134 Spotify              => (docker) Lecteur de musique\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "OPTIONS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 0 Quitter                => Quitter le programme d'installation\n"
          "\n"
          "\033[36;1m")

# CHOIX DU MENU
    try:
        choixMenu = raw_input("\033[36;1m" "VEUILLEZ SAISIR VOTRE CHOIX : " "\033[36;1m")
        choixMenu = str(choixMenu)

# QUITTER LE MENU
        if choixMenu == "0":
            print("\033[36;1m" "\nMerci aurevoir\n" "\033[36;1m")
            programmeLancer = False

# MODULES CONFIGURATION
        elif choixMenu == "1":
            import configuration.kalibuild
            continue

        elif choixMenu == "2":
            import configuration.sourceslist
            continue

        elif choixMenu == "3":
            import configuration.gnomemini
            continue

        elif choixMenu == "4":
            import configuration.themesombre
            continue

        elif choixMenu == "5":
            import configuration.bluetooth
            continue

        elif choixMenu == "6":
            import configuration.son
            continue

        elif choixMenu == "7":
            import configuration.grub
            continue

        elif choixMenu == "8":
            import configuration.grubimg
            continue

        elif choixMenu == "9":
            import configuration.vimrc
            continue

        elif choixMenu == "10":
            import configuration.terminalcustom
            continue

        elif choixMenu == "11":
            import configuration.conky
            continue

        elif choixMenu == "12":
            import configuration.htop
            continue

        elif choixMenu == "13":
            import configuration.autoclean
            continue

        elif choixMenu == "14":
            import configuration.autodestruction
            continue

# MODULES ANONYMAT
        elif choixMenu == "20":
            import anonymat.hostnamerandom
            continue

        elif choixMenu == "21":
            import anonymat.macrandom
            continue

        elif choixMenu == "23":
            import anonymat.iprandom
            continue

        elif choixMenu == "24":
            import anonymat.torprivoxy
            continue

# MODULES VIRTUALISATION
        elif choixMenu == "30":
            import virtualisation.virtualbox
            continue

        elif choixMenu == "31":
            import virtualisation.docker
            continue

# MODULES FIREWALL
        elif choixMenu == "40":
            import firewall.snort
            continue

        elif choixMenu == "41":
            import firewall.dnscrypt
            continue

        elif choixMenu == "42":
            import firewall.noip
            continue

# MODULES PENTEST
        elif choixMenu == "50":
            import pentest.armitage
            continue

        elif choixMenu == "51":
            import pentest.gophish
            continue

        elif choixMenu == "52":
            import pentest.onionscan
            continue

        elif choixMenu == "53":
            import pentest.ufonet
            continue

        elif choixMenu == "54":
            import pentest.cupp
            continue

        elif choixMenu == "55":
            import pentest.webshell
            continue

        elif choixMenu == "56":
            import pentest.sqlmap
            continue

        elif choixMenu == "57":
            import pentest.maltego
            continue

        elif choixMenu == "58":
            import pentest.wifite
            continue

        elif choixMenu == "59":
            import pentest.nikto
            continue

        elif choixMenu == "60":
            import pentest.whatweb
            continue

# MODULES CMS
        elif choixMenu == "70":
            import cms.pelican
            continue

# MODULES NAVIGATEURS
        elif choixMenu == "80":
            import navigateurs.firefox
            continue

        elif choixMenu == "81":
            import navigateurs.opera
            continue

        elif choixMenu == "82":
            import navigateurs.torbrowser
            continue

# MODULES MESSAGERIES
        elif choixMenu == "90":
            import messageries.pidgin
            continue

        elif choixMenu == "91":
            import messageries.discord
            continue

# MODULES CLOUDS
        elif choixMenu == "100":
            import clouds.dropbox
            continue

# MODULES CONTROLE DISTANT
        elif choixMenu == "110":
            import controledistant.teamviewer
            continue

# MODULES CHIFFREMENTS
        elif choixMenu == "120":
            import chiffrements.keepassx
            continue

        elif choixMenu == "121":
            import chiffrements.peazip
            continue

# MODULES OUTILS
        elif choixMenu == "130":
            import outils.atom
            continue

        elif choixMenu == "131":
            import outils.libreoffice
            continue

        elif choixMenu == "132":
            import outils.obs
            continue

        elif choixMenu == "133":
            import outils.openshot
            continue

        elif choixMenu == "134":
            import outils.spotify
            continue

# GESTION ERREUR
        else:
            print("\033[36;1m" "\nCe choix n'est pas dans la liste\n" "\033[36;1m")
            continue

    except KeyboardInterrupt:
        print("\033[36;1m" "\nMerci aurevoir\n" "\033[36;1m")
        programmeLancer = False

    except ImportError:
        print("\033[36;1m" "\nImpossible de trouver le module\n" "\033[36;1m")
        continue

    except:
        print("\033[36;1m" "\nVous devez saisir un nombre\n" "\033[36;1m")
        continue
