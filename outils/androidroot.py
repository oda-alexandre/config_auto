# coding:utf-8

'''
module pour l'installation de android root tools via docker
'''

import os

# INSTALLATION DEPUIS LE DOCKER HUB
print("\033[36;1m \nInstallation de android root tools\n \033[0m")

os.system("docker run -ti --rm --name android-root-tools -v ${HOME}:/home/android -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/bus/usb:/dev/bus/usb --privileged --env=QT_X11_NO_MITSHM=1 -v ${XAUTHORITY}:/xauthority:ro -e XAUTHORITY='/xauthority' -e DISPLAY alexandreoda/android-root-tools")

# AJOUT D'UN ALIAS DANS LE .bashrc
os.system("echo \"alias docker-wifite=\"docker run -ti --rm --name android-root-tools -v ${HOME}:/home/android -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v /dev/bus/usb:/dev/bus/usb --privileged --env=QT_X11_NO_MITSHM=1 -v ${XAUTHORITY}:/xauthority:ro -e XAUTHORITY='/xauthority' -e DISPLAY alexandreoda/android-root-tools\"\" >> $HOME/.bashrc")
