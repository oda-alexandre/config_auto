# coding:utf-8

'''
module for the personnalisation wallpaper of grub
'''

import os

# CHANGE OF THE IMAGE OF WALLPAPER OF GRUB /boot/grub/.background_cache.png
print("\033[36;1m \nput your image background_cache.png in your personal folder\n \033[0m")

enter = raw_input("\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")

print("\033[36;1m \nChange wallpaper of grub\n \033[0m")

os.system("sudo rm -f /boot/grub/.background_cache.png && \
sudo mv $HOME/background_cache.png /boot/grub/background_cache.png")

# UPDATE OF GRUB FOR TAKING OF THE CHANGES
os.system("sudo update-grub")
