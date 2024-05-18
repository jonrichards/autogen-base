FROM mcr.microsoft.com/vscode/devcontainers/python:3.12

# Install Docker CLI
RUN sudo apt update && \
    sudo apt install -y docker.io

# Install pip requirements
COPY requirements.txt /tmp/pip-tmp/
RUN pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
