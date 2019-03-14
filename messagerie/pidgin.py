# coding:utf-8

'''
module pour l'installation de pidgin via docker
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallations de pidgin\n \033[0m")

os.system("docker run -d --name pidgin -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/pidgin -e DISPLAY alexandreoda/pidgin")

# CONSIGNES DE CONFIGURATION
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
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
