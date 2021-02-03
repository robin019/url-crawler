FROM python:3.8

WORKDIR /url_crawler

COPY . /url_crawler

RUN pip install pipenv \
    && pipenv install --system --deploy