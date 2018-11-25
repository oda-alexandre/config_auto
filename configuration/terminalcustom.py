# coding:utf-8

'''
module pour l'installation de terminator et la mise en place du fichier .bashrc personnailer
'''

print("\033[36;1m \nInstallation des prerequis\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
terminator")

print("\033[36;1m \nInstallation du fichier .bashrc\n \033[0m")

os.system("git clone https://github.com/oda-alexandre/terminal-custom.git && \
cp terminal_custom/bashrc $HOME/.bashrc && \
sudo cp terminal_custom/bashrc /root/.bashrc && \
rm -rf terminal_custom")

continue
