FROM python:3

RUN apt-get update -y
RUN apt-get install -y curl
RUN pip3 install flask

WORKDIR /app

COPY ./flag.txt /flag.txt
COPY ./stuff/readflag /readflag
COPY ./stuff/app.py ./app.py
RUN chmod 400 /flag.txt
RUN chmod 111 /readflag
RUN chmod +s /readflag
RUN chmod +x ./app.py
RUN useradd -m app
RUN mkdir /app/outputs
RUN chown app /app/outputs

USER app
CMD [ "/app/app.py" ]