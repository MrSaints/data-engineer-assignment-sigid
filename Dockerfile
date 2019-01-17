FROM python:3.7.1-stretch

WORKDIR /assignment/

COPY requirements.txt /assignment/
RUN pip install -r requirements.txt

COPY . /assignment/
