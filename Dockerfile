FROM python:3.6

RUN mkdir -p /app

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

RUN chmod +x docker-entrypoint.sh

VOLUME /app