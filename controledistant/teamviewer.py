# coding:utf-8

'''
module pour l'installation de teamviewer via docker
'''

print("\033[36;1m \nInstallation de teamviewer\n \033[0m")

os.system("docker run -d --name teamviewer -e DISPLAY -e XAUTHORITY=${XAUTHORITY} -v /tmp/.X11-unix:/tmp/.X11-unix hurricane/teamviewer")

continue
