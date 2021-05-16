FROM nginx:1.19.1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         build-essential \
         nginx \
         python3 \
         python3-dev \
         python3-pip \
         python3-wheel \
         uwsgi \
         uwsgi-plugin-python3 \
         libpcre3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install setuptools

RUN mkdir -p /code/howdareyou
WORKDIR /code/howdareyou
COPY requirements.txt /code/howdareyou
RUN pip3 install -r requirements.txt

RUN apt-get purge -y build-essential && \
    apt-get autoremove -y && \
    apt-get clean -y

WORKDIR /code/howdareyou
COPY . /code/howdareyou

ENV FLASK_APP=howdareyou
ENV FLASK_ENV=production
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN flask run
