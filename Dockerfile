FROM alpine:3.6

MAINTAINER Lukasz Dynowski ludd@bioinformatics.dtu.dk

# Add startup script
ADD scripts/startup.sh /docker/startup.sh

# Copy app dir form host into image
COPY ./app /app
WORKDIR /app

# OS Update & Upgrade
RUN apk update && apk upgrade

# Install packages
RUN apk add \
  openssh \
  python \
  py-pip

# Remove temp and cached files
RUN rm  -rf /tmp/* /var/cache/apk/*

# Generate ssh keys
RUN ssh-keygen -A
RUN mkdir -p /var/run/sshd

# Install application wide packages
RUN pip install -r requirements.txt

# Execute script as a global program
RUN ln -s /app/main.py /usr/local/bin/ntcounter
RUN chmod +x /usr/local/bin/ntcounter

# Startup script
ENTRYPOINT ["sh", "/docker/startup.sh"]
