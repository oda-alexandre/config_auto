# coding:utf-8

'''
module pour l'installation de conky avec conky personnaliser
'''

print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommands -y \
psmisc \
conky-manager \
git")

print("\033[36;1m \nInstallation du conky personnaliser\n \033[0m")

os.system("mkdir $HOME/.conky && \
git clone https://github.com/oda-alexandre/conky.git && \
sudo mv conky/conky/pizzadude_bullets /usr/share/fonts && \
cp -r conky/conky $HOME/.conky \
rm -rf conky")

print("\033[36;1m \nDANS LA FENETRE QUI VAS S'OUVRIR SELECTIONNER VOTRE CONKY\n \033[0m")

entree = raw_input("\033[36;1m" "\nAppuyer sur <Entrée> pour continuer\n" "\033[0m")

if entree == "":
    pass
else:
    print("\033[36;1m" "\nVous devez appuyer sur <Entree>\n" "\033[36;1m")
    continue

os.system("conky-manager")

continue
