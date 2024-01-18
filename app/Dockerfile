FROM python:3.10.12-alpine

WORKDIR /app
ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./ ./app

ENTRYPOINT python app/main.py