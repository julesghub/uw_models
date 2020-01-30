FROM underworldcode/underworld2@sha256:a0b5e93729d63daafb84d37438adebad35886e634d172365cd777c32d2f05417

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

COPY . /home/jovyan/workspace/.

USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

