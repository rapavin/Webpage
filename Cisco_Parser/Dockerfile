FROM python:3.8.0-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /home/ec2-user/cisco-app

ADD . /home/ec2-user/cisco-app

COPY ./requirements.txt /home/ec2-user/cisco-app/requirements.txt

RUN pip install -r requirements.txt

COPY . /home/ec2-user/cisco-app
