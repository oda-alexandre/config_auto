# coding:utf-8

'''
module pour la personnalisation du fond d'écran du grub
'''

# MODIFICATION DE L'IMAGE DE FOND D'ECRAN DU GRUB /boot/grub/.background_cache.png
print("\033[36;1m \nPlacez votre image background_cache.png dans votre dossier personnel\n \033[0m")

entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")

    continue

print("\033[36;1m \nModification du fond d'écran du grub\n \033[0m")

os.system("sudo rm -f /boot/grub/.background_cache.png && \
sudo cp $HOME/background_cache.png /boot/grub/background_cache.png")

# MISE A JOUR DU GRUB POUR PRISE EN COMPTE DES MODIFICATIONS
os.system("sudo update-grub")

continue
