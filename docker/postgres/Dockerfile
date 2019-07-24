FROM postgres:latest
RUN echo "ru_RU.UTF-8 UTF-8" > /etc/locale.gen && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen
ENV LANG='ru_RU.utf8' \
    LC_ALL='ru_RU.utf8'
