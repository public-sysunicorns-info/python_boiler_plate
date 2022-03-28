FROM python:3.10 AS builder

# extra dependencies (over what buildpack-deps already includes)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev

# Upgrade Pip
RUN python -m pip install --upgrade pip

# Create Python User on Container
RUN adduser --disabled-password python
USER python
WORKDIR /home/python
ENV PATH="/home/python/.local/bin:${PATH}"

# Prepare Dependencies
COPY --chown=python:python requirements.txt /home/python/wheels/requirements.txt
RUN pip wheel -r /home/python/wheels/requirements.txt -f /home/python/wheels

FROM python:3.10-slim

# Upgrade pip
RUN python -m pip install --upgrade pip

# Create Python User on Container
RUN python -m pip install --upgrade pip
RUN adduser --disabled-password python
USER python
WORKDIR /home/python
ENV PATH="/home/python/.local/bin:${PATH}"

# Retrive previously build wheels
COPY --from=builder /home/python/wheels /home/python/wheels

# Setup Python Env
ENV PATH "/opt/app/src:/root/.local:${PATH}"
ENV PYTHONPATH "/opt/app/src:/root/.local:{$PYTHONPATH}"
ENV LANG C.UTF-8

# Set Image Source
LABEL org.opencontainers.image.source=https://github.com/public-sysunicorns-info/python_boiler_plate

# Port Exposure
EXPOSE 8080

# Copy and Install dependencies as python user
COPY --chown=python:python requirements.txt .
RUN pip install --user -r requirements.txt -f /home/python/wheels

# Clean as Root cache dir
USER root
RUN rm -rf /home/python/wheels && rm -rf /home/python/.cache/pip/*

# Copy Sources Files and set run cmd
USER python
COPY --chown=python:python . .
CMD ["python", "./main.py"]
