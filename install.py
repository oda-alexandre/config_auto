# coding:utf-8

"""
Maintainer:  https://www.oda-alexandre.com/
Description: Configurateur automatisé for Kali Linux
PREREQUISITES:   Python
Tutoriel:    https://www.youtube.com/channel/UCELtTOkvfaLoZzUWZ6zywJQ
"""

# IMPORT OF THE MODULES PYTHON
import os
import sys
import platform

# VERIFICATION OF L'USER EN COURS
if os.geteuid() == 0:

# CREATION D'UN USER EN CAS D'UTILISATION OF COMPTE ROOT
    print("\033[36;1m" "\nCe script ne fonctionne pas en root, un compte user va étre créé" "\033[36;1m")

    os.system("apt install sudo && \
    read -p 'Entrez your nom : ' nom && \
    adduser $nom && \
    adduser $nom sudo && \
    su $nom")

# DEPLACEMENT OF PROGRAMME EN COURS VERS THE personal folder OF NOUVEL USER
    os.system("sudo mv /root/config_auto $HOME/ && \
    python config_auto/install.py")

# VERIFICATION OF L'OS EN COURS
if not platform.platform('kali'):
    sys.exit("\033[36;1m" "\nCe script ne fonctionne que sur une distribution Kali Linux" "\033[36;1m")

# MENU
programmeLancer = True

while programmeLancer:

    print("\033[36;1m"
          "\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "CONFIG\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 1 Kali build             => Création d'une ISO minimal of kali with configurateur automatisé\n"
          " 2 Sources.list           => Change of the sources and update of system\n"
          " 3 Gnome mini             => Configuration minimal of gnome\n"
          " 4 Theme dark           => Utiliser le theme dark integral\n"
          " 5 Bluetooth              => Activation of bluetooth\n"
          " 6 Son                    => Activation of son\n"
          " 7 Grub                   => Acceleration of temps of start-up of grub and display of the logs of boot\n"
          " 8 Grub wallpaper      => Change wallpaper of grub\n"
          " 9 Vimrc                  => Vim with copy/paste & couleur syntax & souri\n"
          " 10 Terminal Custom       => Terminal custom\n"
          " 11 Conky                 => Moniteur systeme personnailer\n"
          " 12 Htop                  => (docker) Moniteur systeme\n"
          " 13 Auto clean            => Cleaning at boot\n"
          " 14 Auto Destruction      => (lvm encrypted) Mot of passe auto destruction\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "ANONYMAT\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 20 Hostname Random       => Change le nom of l'ordinateur at boot\n"
          " 21 Mac Random            => Change les adresses mac at boot\n"
          " 22 Ip Random             => Change IP publique at boot\n"
          " 23 Tor Privoxy           => Passe tout le trafic réseau a travers Tor Privoxy via connection mandataire\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "VIRTUALISATION\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 30 Virtualbox            => Programme of virtualisation\n"
          " 31 Docker                => INSTALL of docker with interface graphique portainer\n"
          " 32 Wine                  => Émulateur of logiciels Windows\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "FIREWALL / IDS / DNS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 40 Snort                 => (docker) Détecteur d'intrusion\n"
          " 41 DnsCrypt              => (docker) Chiffrement dns\n"
          " 42 Noip                  => Synchronisation of l'ip public with Noip toutes les minutes\n"

          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "PENTEST\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 50 Armitage              => en cours of dev (docker) Beef-xss, Msf,Nmap,Geoip via Armitage\n"
          " 51 Gophish               => (docker) Programme of phishing\n"
          " 52 OnionScan             => (docker) Scanner of site .onion\n"
          " 53 Ufonet                => (docker) Programme of Ddos\n"
          " 54 Cupp                  => (docker) Gestion & creation of wordlists\n"
          " 55 WebShell              => Bibliotheque webshell\n"
          " 56 Sqlmap                => (docker) Programme d'injection sql\n"
          " 57 Maltego               => (docker) Programme of footprinting\n"
          " 58 Wifite                => (docker) Programme of crack wifi\n"
          " 59 Nikto                 => (docker) Scanner of serveur web\n"
          " 60 Whatweb               => (docker) Scanner of site web\n"
          " 61 Owasp-Zap             => (docker) Scanner d'application web\n"
          " 62 Wireshark             => (docker) Analyseur of trames web\n"
          " 63 Zenmap                => (docker) Scanner of ports\n"
          " 64 Evilginx              => (docker) Programme of phishing\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CMS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 70 Pelican               => (docker) Générateur of site static\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "NAVIGATEURS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 80 Firefox               => (docker) Navigateur simple\n"
          " 81 Opera                 => (docker) Navigateur with vpn\n"
          " 82 Tor Browser           => (docker) Navigateur of réseau tor\n"
          " 83 Chromium              => (docker) Navigateur google\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "MESSAGERIE\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 90 Pidgin                => (docker) Messagerie instantanée .onion\n"
          " 91 Discord               => (docker) Plateforme Voip\n"
          " 92 Skype                 => (docker) Plateforme Voip\n"
          " 93 Teamspeak client      => (docker) Client for serveur Voip\n"
          " 94 Teamspeak serveur     => (docker) Serveur Voip\n"
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

          " 110 Teamviewer           => (docker) Prise of contrôle à distance\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CHIFFREMENT\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 120 Keepassx             => (docker) Gestionnaire of mot of passe\n"
          " 121 PeaZip               => (docker) Gestionnaire d'archive (zip,rar...)\n"
          " 122 GtkHash              => (docker) Outils of vérification d'intégrité of file\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "TOOLS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 130 Atom                 => (docker) IDE\n"
          " 131 Libreoffice          => (docker) Suite bureautique\n"
          " 132 Obs                  => Capture & streaming video\n"
          " 133 OpenShot             => Editeur video\n"
          " 134 Spotify              => (docker) Lecteur of musique\n"
          " 135 Vlc                  => (docker) Lecteur of media\n"
          " 136 Transmission         => (docker) Téléchargement Torrent\n"
          " 137 Android Studio       => (docker) IDEA\n"
          " 138 Android Root         => (docker) Outils for le root android \n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "OPTIONS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 0 Quitter                => Quitter le programme d'INSTALL\n"
          "\n"
          "\033[36;1m")

# CHOIX OF MENU
    try:
        choixMenu = raw_input("\033[36;1m" "VEUILLEZ SAISIR YOUR CHOIX : " "\033[36;1m")
        choixMenu = str(choixMenu)

# QUITTER THE MENU
        if choixMenu == "0":
            print("\033[36;1m" "\nMerci aurevoir\n" "\033[36;1m")
            programmeLancer = False

# MODULES CONFIG
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
            import configuration.themedark
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

        elif choixMenu == "32":
            import virtualisation.wine
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

        elif choixMenu == "61":
            import pentest.owaspzap
            continue

        elif choixMenu == "62":
            import pentest.wireshark
            continue

        elif choixMenu == "63":
            import pentest.zenmap
            continue

        elif choixMenu == "64":
            import pentest.evilginx
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

        elif choixMenu == "83":
            import navigateurs.chromium
            continue

# MODULES MESSAGERIE
        elif choixMenu == "90":
            import messagerie.pidgin
            continue

        elif choixMenu == "91":
            import messagerie.discord
            continue

        elif choixMenu == "92":
            import messagerie.skype
            continue

        elif choixMenu == "93":
            import messagerie.teamspeakclient
            continue

        elif choixMenu == "94":
            import messagerie.teamspeakserveur
            continue

# MODULES CLOUDS
        elif choixMenu == "100":
            import clouds.dropbox
            continue

# MODULES CONTROLE DISTANT
        elif choixMenu == "110":
            import controledistant.teamviewer
            continue

# MODULES CHIFFREMENT
        elif choixMenu == "120":
            import chiffrement.keepassx
            continue

        elif choixMenu == "121":
            import chiffrement.peazip
            continue

        elif choixMenu == "122":
            import chiffrement.gtkhash
            continue

# MODULES TOOLS
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

        elif choixMenu == "135":
            import outils.vlc
            continue

        elif choixMenu == "136":
            import outils.transmission
            continue

        elif choixMenu == "137":
            import outils.androidstudio
            continue

        elif choixMenu == "138":
            import outils.androidroot
            continue

# GESTION ERREUR
        else:
            print("\033[36;1m" "\nCe choix n'est pas  in  the liste\n" "\033[36;1m")
            continue

    except KeyboardInterrupt:
        print("\033[36;1m" "\nMerci aurevoir\n" "\033[36;1m")
        programmeLancer = False

    except ImportError:
        print("\033[36;1m" "\nImpossible of trouver le module\n" "\033[36;1m")
        continue

    except:
        print("\033[36;1m" "\nVous devez saisir un nombre\n" "\033[36;1m")
        continue
