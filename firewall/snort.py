# coding:utf-8

import os

print("\033[36;1m \nINSTALL FROM THE DOCKER HUB\n \033[0m")

os.system("mkdir $HOME/snort && \
docker run -it --name snort -v ${HOME}/snort:/snort -v ${HOME}/snort:/etc/snort -v ${HOME}/snort:/usr/local/lib -v ${HOME}/snort:/var/log/snort -v /etc/localtime:/etc/localtime:ro --network host --cap-add=NET_ADMIN --restart=always alexandreoda/snort")
