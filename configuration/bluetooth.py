# coding:utf-8

'''
module pour l'activation du bluetooth
'''

print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
bluetooth")

print("\033[36;1m \nActivation du service\n \033[0m")

os.system("sudo systemctl enable bluetooth.service && \
sudo systemctl start bluetooth.service")

continue
