FROM ubuntu:latest

LABEL org.label-schema.name='Autokeras - Ubuntu' \
    org.label-schema.usage='https://github.com/cybersecurity-dev' \
    org.label-schema.url='https://github.com/cybersecurity-dev' \
    org.label-schema.vendor='https://cyberthreatdefence.com/' \
    MAINTAINER="Cyber Threat Defence Center"

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV OPT=/opt
ENV TMP=/tmp

SHELL ["/bin/bash", "-c"]

# Add conda env
COPY conda_workspace_autokeras_cpu.yml $TMP/

# Install base utilities
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y wget \
    && apt-get install -y git-all \
    && apt-get install -y linux-headers-generic \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install miniconda
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

RUN conda init \
    && conda env create -f $TMP/conda_workspace_autokeras_cpu.yml \
    && echo "source activate workspace_autokeras_cpu" >> ~/.bashrc     # Activate the environment

ENV PATH $CONDA_DIR/envs/workspace_autokeras_cpu/bin:$PATH

SHELL ["conda", "run", "--no-capture-output", "-n", "workspace_autokeras_cpu", "/bin/bash", "-c"]
