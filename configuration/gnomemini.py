# coding:utf-8

'''
module pour l'installation de gnome minimaliste avec shell kali linux
'''

print("\033[36;1m \nInstallation des prérequis\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
gdm3 \
gnome-theme-kali \
gnome-session \
gnome-control-center \
gnome-tweaks \
gnome-terminal \
network-manager-gnome \
network-manager-pptp-gnome \
nautilus \
nautilus-extension-gnome-terminal \
gnome-icon-theme \
gnome-disk-utility \
gnome-shell-extensions \
xserver-xorg \
xfonts-base \
kali-defaults \
kali-desktop-live \
desktop-base \
kali-root-login \
sudo \
bash-completion \
net-tools \
gvfs-backends")

print("\033[36;1m \nSuppression des paquets inutiles\n \033[0m")

os.system("sudo apt-get --purge autoremove -y \
chromium* \
chrome* \
firefox-esr \
leafpad \
xpdf \
cherrytree \
evince \
gnome-online-miners \
gnome-online-accounts \
gnome-orca \
gnome-characters \
gnome-contacts \
gnome-shell-extension-easyscreencast \
gnome-system-monitor \
gnome-user-docs \
gnome-font-viewer \
gnome-software-common \
python3-software-properties \
baobab \
florence \
gedit \
file-roller \
gnome-logs \
zim \
yelp \
reportbug \
eog \
vim-gui-common \
vim-common \
vim-tiny")

print("\033[36;1m \nDésactivation des services evolution\n \033[0m")

os.system("sudo mv /usr/lib/evolution/ /usr/lib/evolution-DISABLE/ && \
sudo mv /usr/lib/evolution-data-server/ /usr/lib/evolution-data-server-DISABLE/")

print("\033[36;1m \nSuppressions des dossiers pré-configurés\n \033[0m")

os.system("rm -rf $HOME/Modèles $HOME/Musique $HOME/Public $HOME/Téléchargements $HOME/Vidéos $HOME/Documents $HOME/Images && \
sudo rm -rf /root/Modèles /root/Musique /root/Public /root/Téléchargements /root/Vidéos /root/Documents /root/Images")

continue
