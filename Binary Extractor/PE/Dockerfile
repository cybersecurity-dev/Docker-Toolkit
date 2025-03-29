FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    libfuzzy-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python packages in the virtual environment
RUN pip install --upgrade pip && \
    pip install \
    lief==0.16.4 \
    pandas==2.2.3 \
    ssdeep==3.4 \
    --no-cache-dir

# Set working directory to the volume mount point
WORKDIR /app

# Start with a shell in /app, no automatic execution
ENTRYPOINT ["/bin/bash"]