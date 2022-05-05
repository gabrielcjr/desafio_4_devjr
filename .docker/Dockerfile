FROM python:3.10.4-slim



RUN apt update && apt install -y  --no-install-recommends \
                libyaml-dev \
                gpg \
                gnupg \
                gpg-agent \
                socat \
                git \
                zsh \
                wget \
                curl \
                default-jre \
                fonts-powerline \
                && pip install --no-cache-dir pipenv

RUN useradd -ms /bin/bash python

# USER python

WORKDIR /home/app

COPY . .

# RUN npm install -f nodemon
ENV PYTHONPATH=${PYTHONPATH}/home/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.2/zsh-in-docker.sh)" -- \
    -t https://github.com/romkatv/powerlevel10k \
    -p git \
    -p git-flow \
    -p github \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/zsh-users/zsh-syntax-highlighting \
    -a 'export TERM=xterm-256color'

RUN echo '[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> ~/.zshrc && \
    echo 'HISTFILE=/home/python/zsh/.zsh_history' >> ~/.zshrc && \
    echo 'export GPG_TTY=$(tty)' >> ~/.zshrc

RUN export MYPYPATH=/home/app/src

RUN pipenv sync --dev --pre

