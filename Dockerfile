FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
        less \
        git \
        vim \
        jq \
        libzip-dev \
        zip \
        unzip \
        mariadb-client \
        libjpeg62-turbo \
        libjpeg62-turbo-dev \
        libpng-dev \
        libfreetype6-dev \
        libssl-dev \
        libxml2-dev \
        imagemagick \
        openssl \
        rsync \
	mc

RUN apt-get -y install mc


#WORKDIR /app
WORKDIR /market_place

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY .env .

COPY market_place .
