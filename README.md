# CONFIG AUTO

![kali linux](https://raw.githubusercontent.com/oda-alexandre/config_auto/master/img/logo-kali.png)
## INDEX

- [Introduction](#INTRODUCTION)
- [Prerequis](#PREREQUIS)
- [Installation](#INSTALLATION)
- [License](#LICENSE)


## INTRODUCTION

Ce repository contient un programme de configuration automatiser pour [Kali Linux](https://www.kali.org/), il automatise l'installation et la configuration des programmes suivants :

### CONFIGURATION

- 1 Kali build             => Création d'une ISO minimaliste de kali avec configurateur automatisé
- 2 Sources.list           => Modification des sources.list & update/upgrade/dist-upgrade
- 3 Gnome mini             => Configuration minimaliste de gnome
- 4 Theme sombre           => Utiliser le theme sombre integrale
- 5 Bluetooth              => Activation du bluetooth
- 6 Son                    => Activation du son
- 7 Grub                   => Acceleration du temps de demarrage du grub et affichage des logs de boot
- 8 Grub fond d'ecran      => Modification du fond d'ecran du grub
- 9 Vimrc                  => Vim avec copier/coller & couleur syntax & souris
- 10 Terminal Custom       => Terminal personnaliser
- 11 Conky                 => Moniteur Systeme personnailer
- 12 Htop                  => (docker) Moniteur Systeme terminal
- 13 Auto clean            => Nettoyage a chaque demarrage
- 14 Auto Destruction      => (Pour OS installer en lvm chiffree) Mot de passe auto destruction

### ANONYMAT

- 20 Hostname Random       => Change le nom de l'ordinateur a chaque demarrage
- 21 Mac Random            => Change les adresses mac a chaque demarrage
- 22 Ip Random             => Change l'IP de l'ordinateur a chaque demarrage
- 23 Tor Privoxy           => Passe tout le trafic reseau a travers Tor Privoxy par connection mandataire

### VIRTUALISATION

- 30 Virtualbox            => Programme de virtualisation
- 31 Docker                => Installation de docker avec interface graphique portainer

### FIREWALL / IDS / DNS

- 40 Snort                 => (docker) Detecteur d'intrusion
- 41 DnsCrypt              => (docker) Chiffrement dns
- 42 Noip                  => Synchronisation de l'ip public avec Noip toutes les minutes


### PENTEST

- 50 Armitage              => en cours de dev (docker) Beef-xss, Msf,Nmap,Geoip via Armitage
- 51 Gophish               => (docker) Programme de phishing
- 52 OnionScan             => (docker) Scanner de site .onion
- 53 Ufonet                => (docker) Programme de Ddos
- 54 Cupp                  => (docker) Gestion & creation de wordlists
- 55 WebShell              => Bibliotheque webshell
- 56 Sqlmap                => (docker) Programme d'injection sql
- 57 Maltego               => (docker) Programme de footprinting
- 58 Wifite                => (docker) Programme de crack wifi
- 59 Nikto                 => (docker) Scanner de serveur web
- 60 Whatweb               => (docker) Scanner de site web
- 61 Owasp-Zap             => (docker) Scanner d'application web
- 62 Wireshark             => (docker) Analiseur de trames web
- 63 Zenmap                => (docker) Scanner de ports
- 64 Evilginx              => (docker) Programme de phishing

### CMS

- 70 Pelican               => (docker) Generateur de site static

### NAVIGATEURS

- 80 Firefox               => (docker) Navigateur simple
- 81 Opera                 => (docker) Navigateur avec vpn
- 82 Tor Browser           => (docker) Navigateur du reseau tor
- 83 Chromium              => (docker) Navigateur google

### MESSAGERIES

- 90 Pidgin                => (docker) Messagerie instantanee .onion
- 91 Discord               => (docker) Plateforme Voip
- 92 Skype                 => (docker) Plateforme Voip
- 93 Teamspeak client      => (docker) Client pour Serveur Voip
- 94 Teamspeak serveur     => (docker) Serveur Voip

### CLOUDS

- 100 Dropbox               => (docker) Service Cloud

CONTROLE DISTANT

- 110 Teamviewer           => (docker) Prise de controle a distance

### CHIFFREMENTS

- 120 Keepassx             => (docker) Gestionnaire de mot de passe
- 121 PeaZip               => (docker) Gestionnaire d'archive (zip,rar...)

### OUTILS

- 130 Atom                 => (docker) IDE
- 131 Libreoffice          => (docker) Suite bureautique
- 132 Obs                  => Capture & streaming video
- 133 OpenShot             => Editeur video
- 134 Spotify              => (docker) Lecteur de musique
- 135 Vlc                  => (docker) Lecteur de media
- 136 Transmission         => (docker) Telechargement Torrent
- 137 Android Studio       => (docker) IDEA
- 138 Android Root         => (docker) Outils pour le root android


## PREREQUIS

Utiliser [Kali Linux](https://www.kali.org/)

Installer [Python](https://www.python.org/)


## INSTALLATION

```
git clone https://github.com/oda-alexandre/config_auto.git
```
```
python config_auto/install.py
```


## LICENSE

[![GPLv3+](http://gplv3.fsf.org/gplv3-127x51.png)](https://github.com/oda-alexandre/config_auto/blob/master/LICENSE)
