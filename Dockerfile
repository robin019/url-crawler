FROM python:3.8

RUN pip install pipenv \
    && mkdir -p /var/www/html/url_crawler

WORKDIR /var/www/html/url_crawler

COPY . /var/www/html/url_crawler

RUN pipenv install --system --deploy