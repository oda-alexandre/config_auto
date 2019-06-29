# coding:utf-8

'''
module for install gnome minimal with shell kali linux
'''

import os

# INSTALL PACKAGES
print("\033[36;1m Install of prérequis\n \033[0m")

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
gvfs-backends \
locate \
usbutils \
dosfstools")

# CLEANING UNUSED PACKAGES
print("\033[36;1m \nDeleting unnecessary packages\n \033[0m")

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

# ACTIVATION OF THE INTERFACE eth IN NETWORK MANAGER
print("\033[36;1m \nEnabling the interface eth\n \033[0m")

os.system("echo \"[keyfile]\" | sudo tee -a /usr/lib/NetworkManager/conf.d/10-globally-managed-devices.conf && \
echo \"unmanaged-devices=*,except:type:ethernet,except:type:wifi,except:type:wwan\" | sudo tee -a /usr/lib/NetworkManager/conf.d/10-globally-managed-devices.conf")

# DEACTIVATION OF THE SERVICES EVOLUTION
print("\033[36;1m \nDeactivation of the services evolution\n \033[0m")

os.system("sudo mv /usr/lib/evolution/ /usr/lib/evolution-DISABLE/ && \
sudo mv /usr/lib/evolution-data-server/ /usr/lib/evolution-data-server-DISABLE/")

# CLEANING OF personal folder ROOT AND USER
print("\033[36;1m \nSupp of the folders preconfigured\n \033[0m")

os.system("rm -rf $HOME/Modèles $HOME/Musique $HOME/Public $HOME/Downloads $HOME/Vidéos $HOME/Documents $HOME/Images && \
sudo rm -rf /root/Modèles /root/Musique /root/Public /root/Downloads /root/Vidéos /root/Documents /root/Images")
