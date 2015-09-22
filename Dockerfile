FROM ubuntu:14.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y git
RUN apt-get install -y wget
RUN apt-get install -y python-pip python-dev build-essential
RUN wget http://download.redis.io/releases/redis-3.0.2.tar.gz
RUN tar xzf redis-3.0.2.tar.gz
WORKDIR redis-3.0.2
RUN make
RUN src/redis-server &
RUN mkdir -p /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
