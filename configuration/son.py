# coding:utf-8

'''
module for activation of sound
'''

import os

# INSTALL OF PULSEAUDIO
print("\033[36;1m Install prerequisites\n \033[0m")

os.system("sudo apt update && \
sudo apt install --no-install-recommends -y \
*pulseaudio")
