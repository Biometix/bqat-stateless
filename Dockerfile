FROM amazonlinux:latest

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off
ENV MPLCONFIGDIR=/app/temp

COPY bqat/bqat_core/misc/haarcascade_smile.xml bqat_core/misc/haarcascade_smile.xml

COPY Pipfile /app/

RUN dnf update && dnf install -y mesa-libGL && dnf clean all && \
    python3 -m ensurepip -U; python3 -m pip install 'pip<24.0' --force-reinstall && \
    python3 -m pip install pipenv && \
    pipenv lock; pipenv requirements > requirements.txt && \
    python3 -m pip install -U setuptools && \
    python3 -m pip install -r requirements.txt && \
    pipenv --clear; python3 -m pip uninstall -y pipenv

COPY bqat bqat/
COPY api api/

ARG VER_CORE
ARG VER_API
LABEL BQAT.core.version=$VER_CORE
LABEL BQAT.api.version=$VER_API

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
CMD [ "python3 -m api" ]
