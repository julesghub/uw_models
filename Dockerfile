FROM underworldcode/underworld2@sha256:a0b5e93729d63daafb84d37438adebad35886e634d172365cd777c32d2f05417

COPY . /home/jovyan/workspace/.

USER root
RUN chown -R ${NB_USER}:${NB_USER} /home/jovyan/workspace
USER ${NB_USER}

