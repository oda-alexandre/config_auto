# coding:utf-8

'''
module for install openshot
'''

import os

# INSTALL OF OPENSHOT
print("\033[36;1m Install of openshot\n \033[0m")

os.system("sudo apt-get update && \
sudo apt install --no-install-recommends -y \
openshot")
