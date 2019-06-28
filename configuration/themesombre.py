# coding:utf-8

'''
module for obtenir le théme dark integral
'''

import os

# CONFIG OF FILE .config/gtk-3.0/settings.ini WITH dark-theme
print("\033[36;1m \nConfiguration of file .config/gtk-3.0/settings.ini\n \033[0m")

os.system("mkdir -p $HOME/.config/gtk-3.0 && \
touch $HOME/.config/gtk-3.0/settings.ini && \
echo '[Settings]' >> $HOME/.config/gtk-3.0/settings.ini && \
echo 'gtk-application-prefer-dark-theme=1' >> $HOME/.config/gtk-3.0/settings.ini")
