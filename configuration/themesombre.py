# coding:utf-8

'''
module pour obtenir le théme sombre intégrale
'''

import os

# CONFIGURATION DU FICHIER .config/gtk-3.0/settings.ini AVEC dark-theme
print("\033[36;1m \nConfiguration du fichier .config/gtk-3.0/settings.ini\n \033[0m")

os.system("echo '[Settings]' >> $HOME/.config/gtk-3.0/settings.ini && \
echo 'gtk-application-prefer-dark-theme=1' >> $HOME/.config/gtk-3.0/settings.ini")
