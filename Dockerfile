# ./Dockerfile 
FROM python:3.8.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python -m venv /app/env
ENV PATH="/app/env/bin:$PATH"

#for mysqlclient install
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev

## Install packages
COPY requirements.txt .
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt 


# Make sure we use the virtualenv:
ENV PATH="/app/env/bin:$PATH"
COPY . /app
WORKDIR /app

## Run the application on the port 8000
EXPOSE 8000
