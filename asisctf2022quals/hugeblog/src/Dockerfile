FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt update
RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN pip install Flask pycryptodome flask-session

WORKDIR /home/ctf
ADD ./stuff/app.py    ./
ADD ./stuff/templates ./templates
ADD ./flag.txt  /oh-i-have-the-flag.txt
ADD ./stuff/uwsgi.ini ./
RUN mkdir ./post
RUN chown -R root:ctf ./
RUN chmod -R 550      ./
RUN chown -R ctf:ctf  ./post
RUN chmod    330      ./post

