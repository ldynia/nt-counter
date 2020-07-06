FROM python:3.8.3-alpine

MAINTAINER Lukasz Dynowski ludd@food.dtu.dk

ENV PYTHONUNBUFFERED=True
ENV PYTHONIOENCODING=UTF-8

# Copy app directory
COPY ./app /app
COPY ./test /app/test
COPY ./data /app/data

# Make app working directory
WORKDIR /app

# Create exec user & group
RUN sed -i '/999/d;' /etc/group
RUN addgroup -Sg 999 exec
RUN adduser -SD -h /app -G exec -u 999 exec

# Fix app permissions
RUN chown -R 999:999 /app

# Install application wide packages
RUN pip install pika==1.0.0

# Execute /app/src/main.py as a global program 'ntc'
RUN ln -s /app/src/main.py /usr/local/bin/ntc
RUN chmod +x /usr/local/bin/ntc

# I/O data directory
VOLUME /app/data

USER exec

CMD /bin/sh
