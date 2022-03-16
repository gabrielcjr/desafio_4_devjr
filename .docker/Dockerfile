FROM python:3.10

WORKDIR /home/app

COPY . .

RUN apt-get update -yy \
    && apt-get upgrade -yy \
    && pip install --no-cache-dir pipenv \
    && apt install libyaml-dev gpg gnupg gpg-agent socat zsh npm -yy 

RUN npm install -f nodemon

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.2/zsh-in-docker.sh)" -- \
    -t https://github.com/romkatv/powerlevel10k \
    -p git\
    -p colorize\
    -p github\
    -p vagrant\
    -p virtualenv\
    -p pip\
    -p python\
    -p docker\
    -p https://github.com/zsh-users/zsh-autosuggestions\
    -p docker-compose\
    -p https://github.com/zsh-users/zsh-syntax-highlighting\
    -a 'export TERM=xterm-256-color'

RUN echo '[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> ~/.zshrc && \
    echo 'HISTFILE=/root/zsh/.zsh_history' >> ~/.zshrc

RUN pipenv sync --dev --pre

