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
          " 13 Auto Destruction      => (Pour OS installer en lvm chiffree) Mot de passe auto destruction\n"
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
          "DÉPANNAGE\n"
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
          " 122 Vokoscreen            => Capture video\n"
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
            import configuration.sourceslist

        elif choixMenu == "2":
            import configuration.gnomemini

        elif choixMenu == "3":
            import configuration.themesombre

        elif choixMenu == "4":
            import configuration.bluetooth

        elif choixMenu == "5":
            import configuration.son

        elif choixMenu == "6":
            import configuration.grub

        elif choixMenu == "7":
            import configuration.grubimg

        elif choixMenu == "8":
            import configuration.vimrc

        elif choixMenu == "9":
            import configuration.terminalcustom

        elif choixMenu == "10":
            import configuration.conky

        elif choixMenu == "11":
            import configuration.htop

        elif choixMenu == "12":
            import configuration.autoclean

        elif choixMenu == "13":
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

            print("\033[36;1m \nInstallation de peazip...\n \033[0m")

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
