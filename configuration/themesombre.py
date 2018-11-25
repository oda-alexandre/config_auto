# coding:utf-8

'''
module pour obtenir le théme sombre intégrale
'''

print("\033[36;1m \nConfiguration du fichier .config/gtk-3.0/settings.ini\n \033[0m")

os.system("echo '[Settings]' >> $HOME/.config/gtk-3.0/settings.ini")

os.system("echo 'gtk-application-prefer-dark-theme=1' >> $HOME/.config/gtk-3.0/settings.ini")

continue
