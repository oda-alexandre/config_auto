FROM image source

MAINTAINER contact

# VARIABLES
ENV USER nom
ENV LANG fr_FR.UTF-8
ENV VERSION version
ENV APP lien
ENV PORTS ports
ENV DEBIAN_FRONTEND noninteractive

# INSTALLATION DES PREREQUIS
RUN apt-get update && apt-get install -y --no-install-recommends \
sudo \
ca-certificates \
locales && \

# SELECTION DE LA LANGUE
echo ${LANG} > /etc/locale.gen && locale-gen && \

# AJOUT UTILISATEUR
useradd -d /home/${USER} -m ${USER} && \
passwd -d ${USER} && \
adduser ${USER} sudo && \

# NETTOYAGE
apt-get --purge autoremove -y && \
apt-get autoclean -y && \
rm /etc/apt/sources.list && \
rm -rf /var/cache/apt/archives/* && \
rm -rf /var/lib/apt/lists/*

# SELECTION UTILISATEUR
USER ${USER}

# SELECTION ESPACE DE TRAVAIL
WORKDIR /home/${USER}

# INSTALLATION DE L'APPLICATION
ADD ${APP} /home/${USER}

# AJOUT INCLUDES
COPY ./includes/include.sh /home/${USER}/include.sh

# OUVERTURE DE PORTS
EXPOSE ${PORTS}

# COMMANDE AU DEMARRAGE DU CONTENEUR
CMD commande
