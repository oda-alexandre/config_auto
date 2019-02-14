# coding:utf-8

'''
module pour l'activation du mot de passe autodestruction uniquement disponible pour une installation en LVM chiffrée
'''

import os

# MESSAGE
print("\033[36;1m"
      "\n"
      "DANS LA FENETRE QUI VAS SUIVRE RENSEIGNER COMME CECI :\n\n"

      "1-Entrez votre mot de passe de decryptage (celui utiliser au demarrage du PC)\n"
      "2-Entrez votre mot de passe pour l'auto destruction\n"
      "3-Confirmer le mot de passe pour l'auto destruction\n"
      "\n"
      "\033[0m")

entree = input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

# CONFIGURATION DU MOT DE PASSE AUTO DESTRUCTION AVEC CRYPTSETUP
os.system("sudo cryptsetup luksAddNuke /dev/sda3")
