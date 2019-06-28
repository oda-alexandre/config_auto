# CONFIG AUTO

<img src="https://raw.githubusercontent.com/oda-alexandre/config_auto/master/img/logo-kali.png" width="200" height="200"/>


## INDEX

- [Badges](#BADGES)
- [Introduction](#INTRODUCTION)
- [PREREQUISITESites](#PREREQUISITESITES)
- [Install](#INSTALL)
- [License](#LICENSE)


## BADGES

[![pipeline status](https://gitlab.com/oda-alexandre/config_auto/badges/master/pipeline.svg)](https://gitlab.com/oda-alexandre/config_auto/commits/master)


## INTRODUCTION

This repository contains an automated config program for [Kali Linux](https://www.kali.org/), he automates install the config of the this tools :

> (docker) means that the tool is install by docker

> (lvm encrypted) means that the tool is only available for an encrypted system

### CONFIG

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------------------------------
1 Kali build        | Create a minimal ISO of kali with config_auto integrated
2 Sources.list      | Change of the sources and update of system
3 Gnome mini        | Configuration minimal of gnome
4 Theme dark        | theme dark integral
5 Bluetooth         | Activation of bluetooth
6 Son               | Activation of sound
7 Grub              | Acceleration of temps of start-up of grub and display of the logs of boot
8 Grub wallpaper    | Change wallpaper of grub
9 Vimrc             | Vim with copy/paste & couleur syntax & souri
10 Terminal Custom  | Terminal custom
11 Conky            | Moniteur systeme custom
12 Htop             | (docker) Moniteur systeme
13 Auto clean       | Cleaning at boot
14 Auto Destruction | (lvm encryptede) Mot of passe auto destruction

### ANONYMAT

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
20 Hostname Random  | Change le nom of l'ordinateur at boot
21 Mac Random       | Change les adresses mac at boot
22 Ip Random        | Change IP publique at boot
23 Tor Privoxy      | Passe tout le trafic réseau a travers Tor Privoxy via connection mandataire

### VIRTUALISATION

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
30 Virtualbox       | Programme of virtualisation
31 Docker           | INSTALL of docker with interface graphique portainer

### FIREWALL / IDS / DNS

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
40 Snort            | (docker) Détecteur d'intrusion
41 DnsCrypt         | (docker) Chiffrement dns
42 Noip             | Synchronisation of l'ip public with Noip toutes les minutes

### PENTEST

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
50 Armitage         | en cours of dev (docker) Beef-xss, Msf,Nmap,Geoip via Armitage
51 Gophish          | (docker) Programme of phishing
52 OnionScan        | (docker) Scanner of site .onion
53 Ufonet           | (docker) Programme of Ddos
54 Cupp             | (docker) Gestion & creation of wordlists
55 WebShell         | Bibliotheque webshell
56 Sqlmap           | (docker) Programme d'injection sql
57 Maltego          | (docker) Programme of footprinting
58 Wifite           | (docker) Programme of crack wifi
59 Nikto            | (docker) Scanner of serveur web
60 Whatweb          | (docker) Scanner of site web
61 Owasp-Zap        | (docker) Scanner d'application web
62 Wireshark        | (docker) Analyseur of trames web
63 Zenmap           | (docker) Scanner of ports
64 Evilginx         | (docker) Programme of phishing

### CMS

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
70 Pelican          | (docker) Générateur of site static

### NAVIGATEURS

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
80 Firefox          | (docker) Navigateur simple
81 Opera            | (docker) Navigateur with vpn
82 Tor Browser      | (docker) Navigateur of réseau tor
83 Chromium         | (docker) Navigateur google

### MESSAGERIES

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
90 Pidgin           | (docker) Messagerie instantanée .onion
91 Discord          | (docker) Plateforme Voip
92 Skype            | (docker) Plateforme Voip
93 Teamspeak client | (docker) Client for serveur Voip
94 Teamspeak serveur| (docker) Serveur Voip

### CLOUDS

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
100 Dropbox         | (docker) Service Cloud

### CONTROLE DISTANT

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
110 Teamviewer      | (docker) Prise of contrôle à distance

### CHIFFREMENTS

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
120 Keepassx        | (docker) Gestionnaire of mot of passe
121 PeaZip          | (docker) Gestionnaire d'archive (zip,rar...)

### TOOLS

TOOLS              | DESCRIPTION
--------------------|----------------------------------------------------------
130 Atom            | (docker) IDE
131 Libreoffice     | (docker) Suite bureautique
132 Obs             | Capture & streaming video
133 OpenShot        | Editeur video
134 Spotify         | (docker) Lecteur of musique
135 Vlc             | (docker) Lecteur of media
136 Transmission    | (docker) Téléchargement Torrent
137 Android Studio  | (docker) IDEA
138 Android Root    | (docker) Outils for le root android


## PREREQUISITES

- Utiliser [Kali Linux](https://www.kali.org/)


## INSTALL

```
git clone https://gitlab.com/oda-alexandre/config_auto.git
```
```
python config_auto/install.py
```


## LICENSE

[![GPLv3+](http://gplv3.fsf.org/gplv3-127x51.png)](https://gitlab.com/oda-alexandre/config_auto/blob/master/LICENSE)
