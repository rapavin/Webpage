FROM python:3.8.0-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /Users/praveenselvarajan/Desktop/Cisco_Parser/Cisco_Parser

ADD . /Users/praveenselvarajan/Desktop/Cisco_Parser/Cisco_Parser

COPY ./requirements.txt /Users/praveenselvarajan/Desktop/Cisco_Parser/Cisco_Parser/requirements.txt

RUN pip install -r requirements.txt

COPY . /Users/praveenselvarajan/Desktop/Cisco_Parser/Cisco_Parser