# coding:utf-8

'''
module for install obs studio
'''

import os

# INSTALL OF OBS
print("\033[36;1m Install of obs\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
obs-studio")
