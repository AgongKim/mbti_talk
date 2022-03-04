# ./Dockerfile 
FROM python:3.8.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

## Install packages
COPY requirements.txt ./
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt

## Copy all src files
COPY . .

## Run the application on the port 8000
CMD python manage.py runserver 0:8000
EXPOSE 8000
