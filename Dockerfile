# ./Dockerfile 
FROM python:3.8.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

#for mysqlclient install
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev

## Install packages
COPY requirements.txt /app/requirements.txt
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt 


COPY ./ /app/
WORKDIR /app/

