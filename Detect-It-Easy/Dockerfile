FROM ubuntu:20.04

LABEL org.label-schema.name='Packer Detection - Ubuntu' \
    org.label-schema.usage='https://github.com/cybersecurity-dev' \
    org.label-schema.url='https://github.com/cybersecurity-dev' \
    org.label-schema.vendor='https://cyberthreatdefence.com/' \
    MAINTAINER="Cyber Threat Defence Center"

# Set environment variables
ENV DEBCONF_NOWARNINGS=yes \
    DEBIAN_FRONTEND=noninteractive \
    TERM=xterm-256color \
    PIP_ROOT_USER_ACTION=ignore
ENV OPT=/opt
ENV TMP=/tmp

SHELL ["/bin/bash", "-c"]

RUN mkdir -p /src && mkdir -p die_lin64_portable/base/db

# Install base utilities
RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y autoremove \
    && apt-get autoclean \    
    && apt-get install -y wget tar libglib2.0-0 \
    && apt-get install --quiet --assume-yes linux-headers-generic \
	&& apt-get install -y git-all libicu66 libpcre2-16-0 libdouble-conversion3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN cd /src && git clone https://github.com/horsicq/Detect-It-Easy

RUN wget https://github.com/horsicq/DIE-engine/releases/download/3.10/die_3.10_portable_Ubuntu_20.04_amd64.tar.gz \
    && tar -xzf die_3.10_portable_Ubuntu_20.04_amd64.tar.gz
    
# db update
RUN rm -rf /die_lin64_portable/base/db
RUN cp -r /src/Detect-It-Easy/db /die_lin64_portable/base/db
#ENTRYPOINT ["/die_linux_portable/diec.sh"]

