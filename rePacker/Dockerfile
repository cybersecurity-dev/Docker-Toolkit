FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV OPT=/opt
ENV TMP=/tmp
ENV CONDA_DIR=/opt/conda

RUN mkdir -p $OPT $TMP
COPY conda_workspace_repacker.yml $TMP/

# Install base utilities
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y wget \
    && apt-get install -y git-all cmake \
    && apt-get install -y linux-headers-generic \
    && apt-get install -y xz-utils upx-ucl wine \
    && apt-get install -y unzip libvlccore-dev \
    && apt-get upgrade -y gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p $CONDA_DIR

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

RUN conda env create -f $TMP/conda_workspace_repacker.yml

SHELL ["/bin/bash", "-c"]