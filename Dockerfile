FROM condaforge/miniforge3:latest

# Ustawienie powłoki bash, aby działała aktywacja środowiska
SHELL ["bash", "-c"]

# Inicjalizacja mamby dla powłoki bash – dodaje wymagane wpisy do ~/.bashrc
RUN mamba init bash

WORKDIR /app

# Aktywacja środowiska przy starcie kontenera
CMD ["/bin/bash", "-l"]