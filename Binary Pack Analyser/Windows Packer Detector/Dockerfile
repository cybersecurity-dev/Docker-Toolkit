FROM ubuntu:20.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update package list and install basic dependencies
RUN apt-get update && apt-get -y upgrade && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    unzip \
    git \
    build-essential \
    cmake \
    && apt-get install -y tar libglib2.0-0 \
    && apt-get install --quiet --assume-yes linux-headers-generic \
	&& apt-get install -y git-all libicu66 libpcre2-16-0 libdouble-conversion3 \
    && apt-get -y autoremove \
    && apt-get -y autoclean \ 
    && rm -rf /var/lib/apt/lists/*

# Install Detect-It-Easy (diec)
RUN cd /tmp \
    && wget https://github.com/horsicq/DIE-engine/releases/download/3.10/die_3.10_portable_Ubuntu_20.04_amd64.tar.gz -O /tmp/die.tar.gz \
    && tar -xzf /tmp/die.tar.gz
    
# db update
RUN mkdir -p /usr/local/bin \
    && cp -r /tmp/die_linux_portable/ /usr/local/bin/die_linux_portable/ \
    && chmod +x /usr/local/bin/die_linux_portable/diec.sh && rm /tmp/die.tar.gz

ENV PATH=$PATH:/usr/local/bin/die_linux_portable/

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY check_packer_from_binary.py /app/

# Ensure the script is executable
RUN chmod +x /app/check_packer_from_binary.py

# Set working directory to the volume mount point
WORKDIR /app

# Start with a shell in /app, no automatic execution
ENTRYPOINT ["/bin/bash"]