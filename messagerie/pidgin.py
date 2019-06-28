# coding:utf-8

'''
module for install pidgin by docker
'''

import os

# INSTALL FROM THE DOCKER HUB
print("\033[36;1m \nInstalls of pidgin\n \033[0m")

os.system("docker run -d --name pidgin -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/pidgin -e DISPLAY alexandreoda/pidgin")

# CONSIGNES OF CONFIG
print("\033[36;1m"
      "\nCONFIGURER COMME CECI :\n"
      "(Pour creer un compte XMPP en .onion via tor-browser suivre ce lien libertygb2nyeyay.onion:5280/register_web)\n"

      "\n1-  IN  PIDGIN / TOOLS / PREFERENCES / PROXY :\n"

      "\n(cocher) utiliser une DNS with SOCKS4\n"

      "\nType of proxy	: Tor/Privacy (SOCKS5)\n"
      "\nHote		: 127.0.0.1         Port            : 9050\n"
      "Utilisateur	: laisser vide	Mot of passe	: laisser vide\n"

      "\nACCEPTER THE CERTIFICAT\n"

      "\n2-  IN  PIDGIN / TOOLS / PLUGINS :\n"

      "\n(cocher) Messagerie Confidentielle Off te Record\n"

      "\n3- CHOISIR CONFIGURER THE PLUGIN (a coter of fermer)\n"

      "\n(cliquer) sur produire\n"
      "(cocher) Exiger messagerie privee\n"

      "\n IN  VOS CONVERSATIONS CLIQUER SUR NON-PRIVE / NON-VERIFIER / AUTHENTIFIER THE CONTACT (your interlocuteur devras faire pareil of son cote)\n"
      "\033[0m")

entree = raw_input(
    "\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")
