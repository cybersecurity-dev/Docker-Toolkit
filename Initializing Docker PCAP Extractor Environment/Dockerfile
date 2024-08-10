FROM ubuntu:latest

SHELL ["/bin/bash", "-c"]

# Add conda env
COPY conda_workspace_pcap.yml /tmp

# Install base utilities
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Install miniconda
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

RUN cat /tmp/conda_workspace_pcap.yml

RUN conda env create -f /tmp/conda_workspace_pcap.yml

SHELL ["conda", "run", "--no-capture-output", "-n", "workspace_pcap", "/bin/bash", "-c"]

CMD conda env list
