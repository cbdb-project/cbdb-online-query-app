FROM node:lts-buster-slim AS builder

LABEL maintainer="yiruka114514 <xxx@yyy.zzz>"
LABEL maintainer="IceCodeNew <xxx@yyy.zzz>"

COPY frontend /webapps/
WORKDIR /webapps
RUN npm install \
    && npm run build

################

FROM python:slim AS webserver

LABEL maintainer="yiruka114514 <xxx@yyy.zzz>"
LABEL maintainer="IceCodeNew <xxx@yyy.zzz>"
# ENV PYTHONUNBUFFERED 1

## Installing OS Dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN sed -i -E 's/(deb|security).debian.org/mirrors.cloud.aliyuncs.com/' '/etc/apt/sources.list'
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsqlite3-dev \
    && apt-get -y full-upgrade \
    && apt-get -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false purge \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /webapps/dist /webapps/frontend/dist/
COPY cbdbweb /webapps/cbdbweb/
COPY requirements.txt /webapps/
# COPY requirements-opt.txt /webapps/
WORKDIR /webapps

RUN pip config set global.index-url 'http://mirrors.cloud.aliyuncs.com/pypi/simple' \
    && pip config set global.trusted-host mirrors.cloud.aliyuncs.com
RUN pip install --no-cache-dir -r /webapps/requirements.txt
# RUN pip install --no-cache-dir -r /webapps/requirements-opt.txt

## Django service
EXPOSE 8000
## default command to execute
CMD ["gunicorn", "cbdbweb.wsgi:application", "--bind 127.0.0.1:8000", "--workers 3"]
