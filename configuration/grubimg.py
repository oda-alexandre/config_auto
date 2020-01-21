# coding:utf-8

import os

print("\033[36;1m \nCHANGE WALLPAPER OF GRUB\n \033[0m")

print("\033[36;1m \nput your image background_cache.png in your personal folder\n \033[0m")

enter = raw_input("\033[36;1m" "\nPress <Enter> to continue\n" "\033[0m")

if enter == "":
    pass
else:
    print("\033[36;1m" "\nYou must press <Enter>\n" "\033[36;1m")

os.system("sudo rm -f /boot/grub/.background_cache.png && \
sudo mv $HOME/background_cache.png /boot/grub/background_cache.png")

print("\033[36;1m \nUPDATE GRUB FOR TAKING CHANGES\n \033[0m")

os.system("sudo update-grub")
