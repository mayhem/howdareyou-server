FROM ubuntu:21.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         python3 \
         python3-dev \
         python3-pip \
         python3-wheel \
         uwsgi \
         uwsgi-plugin-python3 \
         libpcre3-dev \
         npm \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install setuptools

RUN mkdir -p /code/howdareyou
WORKDIR /code/howdareyou

COPY requirements.txt /code/howdareyou
RUN pip3 install -r requirements.txt

RUN npm install -D tailwindcss@latest postcss@latest autoprefixer@latest postcss-cli@latest
#RUN npx tailwindcss init tailwind.config.js -m --purge './src/**/*.html' --purge './src/**/*.js'

COPY . /code/howdareyou
RUN node_modules/.bin/postcss static/css/styles.css -o static/css/howdareyou.css

RUN apt-get autoremove -y && \
    apt-get clean -y
 
ENV FLASK_APP=howdareyou.app
ENV FLASK_ENV=production
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD cp admin/nginx/location.conf /vhost/howdareyou.wtf_location && \
    cp admin/nginx/nginx.conf /vhost/howdareyou.wtf && \
    uwsgi -i /code/howdareyou/admin/uwsgi/uwsgi.ini
