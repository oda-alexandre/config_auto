# coding:utf-8

import os

print("\033[36;1m \nCHANGE TIMEOUT GRUB 5 A 1 secondes\n \033[0m")

os.system("sudo sed -i 's/GRUB_TIMEOUT=5/GRUB_TIMEOUT=1/g' /etc/default/grub && \
sudo sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT=\"quiet\"/#GRUB_CMDLINE_LINUX_DEFAULT=\"quiet\"/g' /etc/default/grub && \
sudo update-grub")
