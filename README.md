# CONFIG AUTO

![kali linux](https://raw.githubusercontent.com/oda-alexandre/config_auto/master/img/logo-kali.png)
## INDEX

- [Introduction](#INTRODUCTION)
- [Prerequis](#PREREQUIS)
- [Installation](#INSTALLATION)
- [License](#LICENSE)


## INTRODUCTION

Ce repository contient un programme de configuration automatiser pour [Kali Linux](https://www.kali.org/), il automatise l'installation et la configuration des outils suivants :

> (docker) signifie que l'outils est installer via docker
> (lvm chiffré) signifie que l'outils est disponnible uniquement pour un systéme chiffré

### CONFIGURATION

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------------------------------
1 Kali build        | Création d'une ISO minimaliste de kali avec config_auto intégré
2 Sources.list      | Modification des sources et mise à niveau du systéme
3 Gnome mini        | Configuration minimaliste de gnome
4 Theme sombre      | Thème sombre intégrale
5 Bluetooth         | Activation du bluetooth
6 Son               | Activation du son
7 Grub              | Accélération du temps de démarrage du grub et affichage des logs de boot
8 Grub fond d'écran | Modification du fond d'écran du grub
9 Vimrc             | Vim avec copier/coller & couleur syntax & souri
10 Terminal Custom  | Terminal personnalisé
11 Conky            | Moniteur systeme personnalisé
12 Htop             | (docker) Moniteur systeme
13 Auto clean       | Nettoyage à chaque démarrage
14 Auto Destruction | (lvm chiffrée) Mot de passe auto destruction

### ANONYMAT

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
20 Hostname Random  | Change le nom de l'ordinateur à chaque démarrage
21 Mac Random       | Change les adresses mac à chaque démarrage
22 Ip Random        | Change l'IP publique à chaque démarrage
23 Tor Privoxy      | Passe tout le trafic réseau a travers Tor Privoxy via connection mandataire

### VIRTUALISATION

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
30 Virtualbox       | Programme de virtualisation
31 Docker           | Installation de docker avec interface graphique portainer

### FIREWALL / IDS / DNS

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
40 Snort            | (docker) Détecteur d'intrusion
41 DnsCrypt         | (docker) Chiffrement dns
42 Noip             | Synchronisation de l'ip public avec Noip toutes les minutes

### PENTEST

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
50 Armitage         | en cours de dev (docker) Beef-xss, Msf,Nmap,Geoip via Armitage
51 Gophish          | (docker) Programme de phishing
52 OnionScan        | (docker) Scanner de site .onion
53 Ufonet           | (docker) Programme de Ddos
54 Cupp             | (docker) Gestion & creation de wordlists
55 WebShell         | Bibliotheque webshell
56 Sqlmap           | (docker) Programme d'injection sql
57 Maltego          | (docker) Programme de footprinting
58 Wifite           | (docker) Programme de crack wifi
59 Nikto            | (docker) Scanner de serveur web
60 Whatweb          | (docker) Scanner de site web
61 Owasp-Zap        | (docker) Scanner d'application web
62 Wireshark        | (docker) Analyseur de trames web
63 Zenmap           | (docker) Scanner de ports
64 Evilginx         | (docker) Programme de phishing

### CMS

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
70 Pelican          | (docker) Générateur de site static

### NAVIGATEURS

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
80 Firefox          | (docker) Navigateur simple
81 Opera            | (docker) Navigateur avec vpn
82 Tor Browser      | (docker) Navigateur du réseau tor
83 Chromium         | (docker) Navigateur google

### MESSAGERIES

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
90 Pidgin           | (docker) Messagerie instantanée .onion
91 Discord          | (docker) Plateforme Voip
92 Skype            | (docker) Plateforme Voip
93 Teamspeak client | (docker) Client pour serveur Voip
94 Teamspeak serveur| (docker) Serveur Voip

### CLOUDS

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
100 Dropbox         | (docker) Service Cloud

### CONTROLE DISTANT

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
110 Teamviewer      | (docker) Prise de contrôle à distance

### CHIFFREMENTS

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
120 Keepassx        | (docker) Gestionnaire de mot de passe
121 PeaZip          | (docker) Gestionnaire d'archive (zip,rar...)

### OUTILS

OUTILS              | DESCRIPTION
--------------------|----------------------------------------------------------
130 Atom            | (docker) IDE
131 Libreoffice     | (docker) Suite bureautique
132 Obs             | Capture & streaming video
133 OpenShot        | Editeur video
134 Spotify         | (docker) Lecteur de musique
135 Vlc             | (docker) Lecteur de media
136 Transmission    | (docker) Téléchargement Torrent
137 Android Studio  | (docker) IDEA
138 Android Root    | (docker) Outils pour le root android


## PREREQUIS

- Utiliser [Kali Linux](https://www.kali.org/)

- Installer [Python](https://www.python.org/)


## INSTALLATION

```
git clone https://github.com/oda-alexandre/config_auto.git
```
```
python config_auto/install.py
```


## LICENSE

[![GPLv3+](http://gplv3.fsf.org/gplv3-127x51.png)](https://github.com/oda-alexandre/config_auto/blob/master/LICENSE)
