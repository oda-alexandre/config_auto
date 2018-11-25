# coding:utf-8

'''
module pour l'accélération du temps de démarrage du grub
'''

print("\033[36;1m \nModification timeout /etc/default/grub\n \033[0m")

os.system("sudo sed -i 's/GRUB_TIMEOUT=5/GRUB_TIMEOUT=1/g' /etc/default/grub && \
sudo sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT=\"quiet\"/#GRUB_CMDLINE_LINUX_DEFAULT=\"quiet\"/g' /etc/default/grub && \
sudo update-grub")

continue
