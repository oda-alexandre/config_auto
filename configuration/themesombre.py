# coding:utf-8

import os

print("\033[36;1m \nCONFIG GTK settings.ini WITH dark-theme\n \033[0m")

os.system("mkdir -p $HOME/.config/gtk-*; \
touch $HOME/.config/gtk-*/settings.ini; \
echo '[Settings]' >> $HOME/.config/gtk-*/settings.ini; \
echo 'gtk-application-prefer-dark-theme=1' >> $HOME/.config/gtk-*/settings.ini")
