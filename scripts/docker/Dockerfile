#
# Base stage
#
FROM alpine:3.18.3 as base

RUN apk update

#RUN apk add --update --no-cache libldap \
#                                libssl \
#                                mysql-client \
#                                mariadb-client-libs \
#                                net-tools \
#                                iputils \
#                                bind-tools \
#                                ncurses5-libs \
#                                curl \
#                                libffi-dev \
#                                py-pynacl \
#                                libffi-dev \
#                                libxslt-dev \
#                                gcc \
#                                libc-dev \
#                                python3.11-dev
#     libressl-dev \
RUN apk add --update --no-cache \
    openldap \
    openssl \
    mysql-client \
    net-tools \
    iputils \
    bind-tools \
    ncurses-libs \
    curl \
    libffi-dev \
    py-pynacl \
    libffi-dev \
    libxslt-dev \
    gcc \
    libc-dev \
    python3 \
    py3-pip \
    python3-dev \
    py3-pyldap \
    bash \
    supervisor \
    build-base

RUN pip install --no-cache --upgrade pip
RUN pip install --no-cache virtualenv simple-db-migrate

RUN mkdir -p /netapi

ADD . /netapi/

EXPOSE 8000

WORKDIR /netapi


#
# Build stage
#
FROM base as build

#RUN apk add --update --no-cache python2-dev \
#                                openldap-dev \
#                                libsass-dev \
#                                mariadb-dev \
#                                ncurses-dev \
#                                linux-headers \
#                                gcc \
#                                musl-dev \
#                                libffi-dev \
#                                make
#

RUN apk add --update --no-cache python3 \
                                openldap \
                                py3-pyldap \
                                libsass-dev \
                                mariadb-dev \
                                ncurses-dev \
                                linux-headers \
                                gcc \
                                musl-dev \
                                libffi-dev \
                                make

RUN virtualenv /venv
RUN source /venv/bin/activate
RUN python --version
RUN pip install wheel
RUN pip install gunicorn
# RUN python setup.py bdist_wheel

RUN pip install --upgrade pip setuptools

RUN pip install --no-cache --no-build-isolation -r requirements_debug.txt


#
# Last stage
#
FROM build as image

COPY --from=build /venv /venv
#
#RUN apk add --update --no-cache python3 \
#                                openldap \
#                                py3-pyldap \
#                                libsass-dev \
#                                mariadb-dev \
#                                ncurses-dev \
#                                linux-headers \
#                                gcc \
#                                musl-dev \
#                                libffi-dev \
#                                make
RUN apk add --update --no-cache python3 \
                                libldap \
                                openldap \
                                build-base \
                                openldap-dev \
                                libsass-dev \
                                mariadb-dev \
                                ncurses-dev \
                                linux-headers \
                                gcc \
                                musl-dev \
                                libffi-dev \
                                make \
                                openssl \
                                mysql-client \
                                net-tools \
                                iputils \
                                bind-tools \
                                ncurses-libs \
                                curl \
                                libffi-dev \
                                py-pynacl \
                                libffi-dev \
                                libxslt-dev \
                                gcc \
                                libc-dev \
                                python3 \
                                py3-pip \
                                python3-dev \
                                py3-pyldap \
                                bash \
                                supervisor \
                                build-base
RUN touch /tmp/networkapi.log

ENV PATH="/venv/bin:${PATH}"

ENV PYTHONPATH="/usr/lib/python3.11:/venv/lib/python3.11"

RUN source /venv/bin/activate
RUN pip install --upgrade pip setuptools

RUN pip install --no-cache --no-build-isolation -r requirements.txt

# CMD /netapi/scripts/docker/docker-start-netapi.sh
