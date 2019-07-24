FROM python:3.7-slim-buster
COPY requirements.txt /tmp
COPY docker/app/entrypoint.sh /
RUN apt-get update && \
    apt-get -qq install locales \
        zlib1g-dev \
        gcc \
        python3-dev \
        libpq-dev && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -qq --allow-remove-essential remove gcc python3-dev zlib1g-dev && \
    apt-get -qq autoremove && \
    apt-get clean && \
    echo "ru_RU.UTF-8 UTF-8" > /etc/locale.gen && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen
ENV PYTHONUNBUFFERED=1 \
    LANG='ru_RU.utf8' \
    LC_ALL='ru_RU.utf8'
ENTRYPOINT ["/entrypoint.sh"]
