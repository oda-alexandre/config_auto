# coding:utf-8

"""
Maintainer:     https://www.oda-alexandre.com/
Description:    Automated configurator for Kali Linux
PREREQUISITES:  Python
Tutoriel:       https://www.youtube.com/channel/UCELtTOkvfaLoZzUWZ6zywJQ
"""

# IMPORT OF MODULES PYTHON
import os
import sys
import platform

# VERIFICATION OF USER
if os.geteuid() == 0:

# CREATE USER IF YOUR IS ROOT
    print("\033[36;1m" "\nThis script does not work in root, a user account will be created" "\033[36;1m")

    os.system("apt install sudo && \
    read -p 'Enter your name : ' name && \
    adduser $name && \
    adduser $name sudo && \
    su $name")

# DEPLACEMENT OF THE personal folder OF NEW USER
    os.system("sudo mv /root/config_auto $HOME/ && \
    python config_auto/install.py")

# VERIFICATION OF OS USED
if not platform.platform('kali'):
    sys.exit("\033[36;1m" "\nThis script only works on a Kali Linux distribution" "\033[36;1m")

# MENU
programWorking = True

while programWorking:

    print("\033[36;1m"
          "\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "CONFIG\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 1 Kali build             => Create a minimal ISO of kali with config_auto\n"
          " 2 Sources.list           => Change of the sources and update of system\n"
          " 3 Gnome mini             => Configuration minimal of gnome\n"
          " 4 Theme dark             => Theme dark integral\n"
          " 5 Bluetooth              => Activation of bluetooth\n"
          " 6 Son                    => Activation of sound\n"
          " 7 Grub                   => Acceleration time of start-up grub and display the logs of boot\n"
          " 8 Grub wallpaper         => Change wallpaper of grub\n"
          " 9 Vimrc                  => Vim custom\n"
          " 10 Terminal Custom       => Terminal custom\n"
          " 11 Conky                 => Monitor system custom\n"
          " 12 Htop                  => (docker) Monitor system\n"
          " 13 Auto clean            => Cleaning auto at boot\n"
          " 14 Auto Destruction      => (lvm encryptede) Password for auto destruction\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "ANONYMAT\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 20 Hostname Random       => Hostname random at boot\n"
          " 21 Mac Random            => Mac address random at boot\n"
          " 22 Ip Random             => IP public random at boot\n"
          " 23 Tor Privoxy           => Pass all network over tor privoxy\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "VIRTUALISATION\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 30 Virtualbox            => Virtualisation\n"
          " 31 Docker                => Containerisation\n"
          " 32 Wine                  => Emulator for Windows app (.exe)\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "FIREWALL / IDS / DNS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 40 Snort                 => (docker) Intrusion Detection System\n"
          " 41 DnsCrypt              => (docker) Dns encrypted\n"
          " 42 Noip                  => Synchronisation of ip public with noip all minutes\n"

          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "PENTEST\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 50 Armitage              => In progress...\n"
          " 51 Gophish               => (docker) Programme of phishing\n"
          " 52 OnionScan             => (docker) (docker) Scanner of site of dark net\n"
          " 53 Ufonet                => (docker) Programme of ddos by web servers\n"
          " 54 Cupp                  => (docker) Management & creation of wordlists\n"
          " 55 WebShell              => Bibliotheque webshell\n"
          " 56 Sqlmap                => (docker) Programme of Sql injection\n"
          " 57 Maltego               => (docker) Programme of footprinting\n"
          " 58 Wifite                => (docker) Programme of crack wifi\n"
          " 59 Nikto                 => (docker) Scanner of serveur web\n"
          " 60 Whatweb               => (docker) Scanner of site web\n"
          " 61 Owasp-Zap             => (docker) Scanner of web app\n"
          " 62 Wireshark             => (docker) Analyser of trames\n"
          " 63 Zenmap                => (docker) Scanner of ports\n"
          " 64 Evilginx              => (docker) Programme of phishing\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CMS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 70 Pelican               => (docker) Generator of site static\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "NAVIGATEURS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 80 Firefox               => (docker) Navigator firefox\n"
          " 81 Opera                 => (docker) Navigator with vpn\n"
          " 82 Tor Browser           => (docker) Navigator of tor\n"
          " 83 Chromium              => (docker) Navigator google\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "MESSAGERIE\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 90 Pidgin                => (docker) Instant messaging\n"
          " 91 Discord               => (docker) Plateform Voip\n"
          " 92 Skype                 => (docker) Plateform Voip\n"
          " 93 Teamspeak client      => (docker) Client Voip\n"
          " 94 Teamspeak serveur     => (docker) Serveur Voip\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CLOUDS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 100 Dropbox              => (docker) Cloud\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CONTROLE DISTANT\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 110 Teamviewer           => (docker) Support control\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "CHIFFREMENT\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 120 Keepassx             => (docker) Management of password\n"
          " 121 PeaZip               => (docker) Management archive (zip,rar...)\n"
          " 122 GtkHash              => (docker) Tools of integrity check of file\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "TOOLS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 130 Atom                 => (docker) IDE\n"
          " 131 Libreoffice          => (docker) Office suite\n"
          " 132 Obs                  => Streaming video\n"
          " 133 OpenShot             => Editor video\n"
          " 134 Spotify              => (docker) Reader of musique\n"
          " 135 Vlc                  => (docker) Reader of media\n"
          " 136 Transmission         => (docker) Download Torrent\n"
          " 137 Android Studio       => (docker) IDEA\n"
          " 138 Android Root         => (docker) Tools for root android \n"
          " 139 VSCode               => (docker) IDE\n"
          "\n"

          "-----------------------------------------------------------------------------------------------------------------\n"
          "OPTIONS\n"
          "-----------------------------------------------------------------------------------------------------------------\n"
          "\n"

          " 0 Quit                => Quit the programme\n"
          "\n"
          "\033[36;1m")

# CHOIX OF MENU
    try:
        choiceMenu = raw_input("\033[36;1m" "ENTER YOUR CHOICE : " "\033[36;1m")
        choiceMenu = str(choiceMenu)

# QUIT THE MENU
        if choiceMenu == "0":
            print("\033[36;1m" "\nGoodbye\n" "\033[36;1m")
            programWorking = False

# MODULES CONFIG
        elif choiceMenu == "1":
            import configuration.kalibuild
            continue

        elif choiceMenu == "2":
            import configuration.sourceslist
            continue

        elif choiceMenu == "3":
            import configuration.gnomemini
            continue

        elif choiceMenu == "4":
            import configuration.themedark
            continue

        elif choiceMenu == "5":
            import configuration.bluetooth
            continue

        elif choiceMenu == "6":
            import configuration.son
            continue

        elif choiceMenu == "7":
            import configuration.grub
            continue

        elif choiceMenu == "8":
            import configuration.grubimg
            continue

        elif choiceMenu == "9":
            import configuration.vimrc
            continue

        elif choiceMenu == "10":
            import configuration.terminalcustom
            continue

        elif choiceMenu == "11":
            import configuration.conky
            continue

        elif choiceMenu == "12":
            import configuration.htop
            continue

        elif choiceMenu == "13":
            import configuration.autoclean
            continue

        elif choiceMenu == "14":
            import configuration.autodestruction
            continue

# MODULES ANONYMAT
        elif choiceMenu == "20":
            import anonymat.hostnamerandom
            continue

        elif choiceMenu == "21":
            import anonymat.macrandom
            continue

        elif choiceMenu == "23":
            import anonymat.iprandom
            continue

        elif choiceMenu == "24":
            import anonymat.torprivoxy
            continue

# MODULES VIRTUALISATION
        elif choiceMenu == "30":
            import virtualisation.virtualbox
            continue

        elif choiceMenu == "31":
            import virtualisation.docker
            continue

        elif choiceMenu == "32":
            import virtualisation.wine
            continue

# MODULES FIREWALL
        elif choiceMenu == "40":
            import firewall.snort
            continue

        elif choiceMenu == "41":
            import firewall.dnscrypt
            continue

        elif choiceMenu == "42":
            import firewall.noip
            continue

# MODULES PENTEST
        elif choiceMenu == "50":
            import pentest.armitage
            continue

        elif choiceMenu == "51":
            import pentest.gophish
            continue

        elif choiceMenu == "52":
            import pentest.onionscan
            continue

        elif choiceMenu == "53":
            import pentest.ufonet
            continue

        elif choiceMenu == "54":
            import pentest.cupp
            continue

        elif choiceMenu == "55":
            import pentest.webshell
            continue

        elif choiceMenu == "56":
            import pentest.sqlmap
            continue

        elif choiceMenu == "57":
            import pentest.maltego
            continue

        elif choiceMenu == "58":
            import pentest.wifite
            continue

        elif choiceMenu == "59":
            import pentest.nikto
            continue

        elif choiceMenu == "60":
            import pentest.whatweb
            continue

        elif choiceMenu == "61":
            import pentest.owaspzap
            continue

        elif choiceMenu == "62":
            import pentest.wireshark
            continue

        elif choiceMenu == "63":
            import pentest.zenmap
            continue

        elif choiceMenu == "64":
            import pentest.evilginx
            continue

# MODULES CMS
        elif choiceMenu == "70":
            import cms.pelican
            continue

# MODULES NAVIGATEURS
        elif choiceMenu == "80":
            import navigateurs.firefox
            continue

        elif choiceMenu == "81":
            import navigateurs.opera
            continue

        elif choiceMenu == "82":
            import navigateurs.torbrowser
            continue

        elif choiceMenu == "83":
            import navigateurs.chromium
            continue

# MODULES MESSAGERIE
        elif choiceMenu == "90":
            import messagerie.pidgin
            continue

        elif choiceMenu == "91":
            import messagerie.discord
            continue

        elif choiceMenu == "92":
            import messagerie.skype
            continue

        elif choiceMenu == "93":
            import messagerie.teamspeakclient
            continue

        elif choiceMenu == "94":
            import messagerie.teamspeakserveur
            continue

# MODULES CLOUDS
        elif choiceMenu == "100":
            import clouds.dropbox
            continue

# MODULES SUPPORT
        elif choiceMenu == "110":
            import controledistant.teamviewer
            continue

# MODULES CHIFFREMENT
        elif choiceMenu == "120":
            import chiffrement.keepassx
            continue

        elif choiceMenu == "121":
            import chiffrement.peazip
            continue

        elif choiceMenu == "122":
            import chiffrement.gtkhash
            continue

# MODULES TOOLS
        elif choiceMenu == "130":
            import outils.atom
            continue

        elif choiceMenu == "131":
            import outils.libreoffice
            continue

        elif choiceMenu == "132":
            import outils.obs
            continue

        elif choiceMenu == "133":
            import outils.openshot
            continue

        elif choiceMenu == "134":
            import outils.spotify
            continue

        elif choiceMenu == "135":
            import outils.vlc
            continue

        elif choiceMenu == "136":
            import outils.transmission
            continue

        elif choiceMenu == "137":
            import outils.androidstudio
            continue

        elif choiceMenu == "138":
            import outils.androidroot
            continue

        elif choiceMenu == "139":
            import outils.vscode
            continue

# MANAGEMENT ERROR
        else:
            print("\033[36;1m" "\nThis choice is not in the list\n" "\033[36;1m")
            continue

    except KeyboardInterrupt:
        print("\033[36;1m" "\nGoodbye\n" "\033[36;1m")
        programWorking = False

    except ImportError:
        print("\033[36;1m" "\Module not found\n" "\033[36;1m")
        continue

    except:
        print("\033[36;1m" "\nYou must enter a number\n" "\033[36;1m")
        continue
