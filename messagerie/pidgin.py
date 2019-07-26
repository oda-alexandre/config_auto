# coding:utf-8

import os

print("\033[36;1m \nINSTALL FROM THE DOCKER HUB\n \033[0m")

os.system("docker run -d --name pidgin -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/pidgin -e DISPLAY alexandreoda/pidgin")

print("\033[36;1m"
      "\nCONFIGURE LIKE THIS :\n"
      "(To create an XMPP account in .onion via tor-browser follow this link libertygb2nyeyay.onion:5280/register_web)\n"

      "\n1-  IN  PIDGIN / TOOLS / PREFERENCES / PROXY :\n"

      "\n(check) Use a DNS with SOCKS4\n"

      "\nType of proxy	: Tor/Privacy (SOCKS5)\n"
      "\nHote	      	: 127.0.0.1          Port            : 9050\n"
      "USER           	: laisser vide       Mot of passe    : laisser vide\n"

      "\nACCEPT THE CERTIFICAT\n"

      "\n2-  IN  PIDGIN / TOOLS / PLUGINS :\n"

      "\n(check) Messaging Confidential Off te Record\n"

      "\n3- CHOICE CONFIGURE THE PLUGIN (next to closed)\n"

      "\n(clic) on produce\n"
      "(check) Require private messaging\n"

      "\nIN YOUR CONVERSATIONS CLIC ON NO-PRIVATE / NO-CHECK / AUTHENTICATE THE CONTACT (your interlocutor will have to do the same)\n"
      "\033[0m")

enter = raw_input(
    "\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")
