# CONFIG AUTO

<img src="https://raw.githubusercontent.com/oda-alexandre/config_auto/master/img/logo-kali.png" width="200" height="200"/>

## INDEX

- [Badges](#BADGES)
- [Introduction](#INTRODUCTION)
- [Prerequisites](#PREREQUISITESITES)
- [Install](#INSTALL)
- [License](#LICENSE)

## BADGES

[![pipeline status](https://gitlab.com/oda-alexandre/config_auto/badges/master/pipeline.svg)](https://gitlab.com/oda-alexandre/config_auto/commits/master)

## INTRODUCTION

This repository contains an automated config program for

- [Kali Linux](https://www.kali.org/), he automates install the config of this tools :

> (docker) means that the tool is install by docker
> (lvm encrypted) means that the tool is only available for an encrypted system

### CONFIG

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------------------------------
1 Kali build        | Create a minimal ISO of kali with config_auto integrated
2 Sources.list      | Change of the sources and update of system
3 Gnome mini        | Configuration minimal of gnome
4 Theme dark        | Theme dark integral
5 Bluetooth         | Activation of bluetooth
6 Son               | Activation of sound
7 Grub              | Acceleration time of start-up grub and display the logs of boot
8 Grub wallpaper    | Change wallpaper of grub
9 Vimrc             | Vim custom
10 Terminal Custom  | Terminal custom
11 Conky            | Monitor system custom
12 Htop             | (docker) Monitor system
13 Auto clean       | Cleaning auto at boot
14 Auto Destruction | (lvm encryptede) Password for auto destruction

### ANONYMAT

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
20 Hostname Random  | Hostname random at boot
21 Mac Random       | Mac address random at boot
22 Ip Random        | IP public random at boot
23 Tor Privoxy      | Pass all network over tor privoxy

### VIRTUALISATION

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
30 Virtualbox       | Virtualisation
31 Docker           | Containerisation
32 Wine             | Emulator for Windows app (.exe)

### FIREWALL / IDS / DNS

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
40 Snort            | (docker) Intrusion Detection System
41 DnsCrypt         | (docker) Dns encrypted
42 Noip             | Synchronisation of ip public with noip all minutes

### PENTEST

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
50 Armitage         | In progress...
51 Gophish          | (docker) Programme of phishing
52 OnionScan        | (docker) Scanner of site of dark net
53 Ufonet           | (docker) Programme of ddos by web servers
54 Cupp             | (docker) Management & creation of wordlists
55 WebShell         | Library of webshell
56 Sqlmap           | (docker) Programme of Sql injection
57 Maltego          | (docker) Programme of footprinting
58 Wifite           | (docker) Programme of crack wifi
59 Nikto            | (docker) Scanner of serveur web
60 Whatweb          | (docker) Scanner of site web
61 Owasp-Zap        | (docker) Scanner of web app
62 Wireshark        | (docker) Analyser of trames
63 Zenmap           | (docker) Scanner of ports
64 Evilginx         | (docker) Programme of phishing

### CMS

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
70 Pelican          | (docker) Generator of site static

### NAVIGATOR

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
80 Firefox          | (docker) Navigator firefox
81 Opera            | (docker) Navigator with vpn
82 Tor Browser      | (docker) Navigator of tor
83 Chromium         | (docker) Navigator google

### MESSAGING

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
90 Pidgin           | (docker) Instant messaging
91 Discord          | (docker) Plateform Voip
92 Skype            | (docker) Plateform Voip
93 Teamspeak client | (docker) Client Voip
94 Teamspeak serveur| (docker) Serveur Voip

### CLOUDS

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
100 Dropbox         | (docker) Cloud

### SUPPORT

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
110 Teamviewer      | (docker) Support control

### CHIFFREMENTS

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
120 Keepassx        | (docker) Management of password
121 PeaZip          | (docker) Management archive (zip,rar...)
122 GtkHash         | (docker) Tools of integrity check of file

### TOOLS

TOOLS               | DESCRIPTION
--------------------|----------------------------------------------------------
130 Atom            | (docker) IDE
131 Libreoffice     | (docker) Office suite
132 Obs             | Streaming video
133 OpenShot        | Editor video
134 Spotify         | (docker) Reader of musique
135 Vlc             | (docker) Reader of media
136 Transmission    | (docker) Download Torrent
137 Android Studio  | (docker) IDEA
138 Android Root    | (docker) Tools for root android

## PREREQUISITES

- Use [Kali Linux](https://www.kali.org/)

## INSTALL

```git clone https://gitlab.com/oda-alexandre/config_auto.git```

```python config_auto/install.py```

## LICENSE

[![GPLv3+](http://gplv3.fsf.org/gplv3-127x51.png)](https://gitlab.com/oda-alexandre/config_auto/blob/master/LICENSE)
