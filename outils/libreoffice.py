# coding:utf-8

'''
module pour l'installation de libreoffice via docker
'''

print("\033[36;1m \nInstallation de libreoffice\n \033[0m")

os.system("docker run -d --name libreoffice -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ${HOME}:/home/libreoffice -e DISPLAY --network none alexandreoda/libreoffice")

continue
