# coding:utf-8

import os

print("\033[36;1m \nINSTALL PREREQUISITES\n \033[0m")

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

print("\033[36;1m \nCLEANING UNUSED PACKAGES\n \033[0m")

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

print("\033[36;1m \nACTIVATION eth IN NETWORK MANAGER\n \033[0m")

os.system("echo \"[keyfile]\" | sudo tee -a /usr/lib/NetworkManager/conf.d/10-globally-managed-devices.conf && \
echo \"unmanaged-devices=*,except:type:ethernet,except:type:wifi,except:type:wwan\" | sudo tee -a /usr/lib/NetworkManager/conf.d/10-globally-managed-devices.conf")