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
    mariadb-client \
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
    py3-pip

RUN pip install --no-cache --upgrade pip
RUN pip install --no-cache virtualenv

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

RUN apk add --update --no-cache python3 \
                                openldap \
                                libsass-dev \
                                mariadb-dev \
                                ncurses-dev \
                                linux-headers \
                                gcc \
                                musl-dev \
                                libffi-dev \
                                make

RUN virtualenv /venv && \
    source /venv/bin/activate && \
    python --version \
    pip install --no-cache --no-build-isolation -r requirements_debug.txt


#
# Last stage
#
FROM base as image

COPY --from=build /venv /venv

RUN touch /tmp/networkapi.log

ENV PATH="/venv/bin:${PATH}"

ENV PYTHONPATH="/usr/lib/python3.11:/venv/lib/python3.11"

# CMD /netapi/scripts/docker/docker-start-netapi.sh
