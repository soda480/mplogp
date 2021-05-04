FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /mplogp

COPY . /mplogp/

RUN apk --update --no-cache add gcc libc-dev libffi-dev openssl-dev
RUN pip install twine
RUN pip install pybuilder
RUN pyb install
