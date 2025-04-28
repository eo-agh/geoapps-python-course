# Use Miniforge3 as base image - it comes with mamba pre-installed
FROM condaforge/miniforge3:latest

# Set bash as the default shell
ENV SHELL=/bin/bash

# Set working directory
WORKDIR /app

# Install make and other system dependencies
RUN apt-get update && \
    apt-get install -y make && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the entire project
COPY . .

# Install conda-lock and create the environment in a single layer
RUN mamba init bash && \
    . /root/.bashrc && \
    mamba install -y -c conda-forge conda-lock && \
    conda-lock install --mamba -n geoapps-env conda-lock-dev.yml && \
    mamba clean -afy && \
    echo "mamba activate geoapps-env" >> ~/.bashrc

# Install the package in editable mode
RUN mamba run -n geoapps-env pip install -e .

# Just start bash
CMD ["/bin/bash"]
