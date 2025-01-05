# Use an official Ubuntu base image
FROM ubuntu:12.04

LABEL org.label-schema.name='xv6 Development - Ubuntu' \
    org.label-schema.usage='https://github.com/cybersecurity-dev' \
    org.label-schema.url='https://github.com/cybersecurity-dev' \
    org.label-schema.vendor='https://cyberthreatdefence.com/' \
    MAINTAINER="Cyber Threat Defence Center"

RUN sed -i 's|http://archive.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/ubuntu|g' /etc/apt/sources.list
RUN sed -i 's|http://security.ubuntu.com/ubuntu|http://old-releases.ubuntu.com/ubuntu|g' /etc/apt/sources.list

# Install necessary packages
RUN apt-get update && apt-get install -y \
    gcc-4.6 build-essential \
    bison \
    flex \
    libncurses5-dev \
    wget \
    bin86 \
    binutils \
    gcc-multilib \
    qemu \
    git \
    nasm \
    gdb \
    make

# Set the working directory
WORKDIR /usr/src/xv6

# Clone the xv6 repository
RUN git clone https://github.com/mit-pdos/xv6-public.git /usr/src/xv6

# Set the CFLAGS environment variable to disable the array-bounds warning2
# error: array subscript -48806446 is outside array bounds of 'void[2147483647]'
ENV CFLAGS="-Wno-error=array-bounds"

# Compile the xv6 operating system
RUN make 

RUN cp fs.img /mnt/shared/ && cp xv6.img /mnt/shared/

# Set the default command to run when the container starts
CMD ["bash"]