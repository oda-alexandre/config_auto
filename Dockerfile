FROM kalilinux/kali-linux-docker

LABEL authors https://www.oda-alexandre.com/

ENV USER kali

RUN echo -e '\033[36;1m ******* INSTALL APP ******** \033[0m' && \
  apt update && apt install --no-install-recommends -y \
  sudo \
  python

RUN echo -e '\033[36;1m ******* ADD USER ******** \033[0m' && \
  useradd -d ${HOME} -m ${USER} && \
  passwd -d ${USER} && \
  adduser ${USER} sudo

RUN echo -e '\033[36;1m ******* SELECT USER ******** \033[0m'
USER ${USER}

RUN echo -e '\033[36;1m ******* SELECT WORKING SPACE ******** \033[0m'
WORKDIR ${HOME}

RUN echo -e '\033[36;1m ******* ADD APP ******** \033[0m'
COPY ./  ${HOME}/

RUN echo -e '\033[36;1m ******* CONTAINER START COMMAND ******** \033[0m'
CMD python install.py