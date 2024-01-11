FROM python:3.9.6-alpine

WORKDIR /app/
ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./ ./app

ENTRYPOINT python app/main.py 