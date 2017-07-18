FROM alpine:3.6

MAINTAINER Lukasz Dynowski ludd@bioinformatics.dtu.dk

# Set environment variables
ENV PATH $PATH:/usr/local/bin

# Create pipline common directories
VOLUME ["/pipeline/data", "/pipeline/results"]

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

# Generate ssh keys and set up ssh config
RUN mkdir -p /var/run/sshd /root/.ssh
RUN ssh-keygen -A
RUN sed -i 's/#PermitUserEnvironment no/PermitUserEnvironment yes/' /etc/ssh/sshd_config
RUN echo "PATH=$PATH" >> /root/.ssh/environment

# Install application wide packages
RUN pip install -r requirements.txt

# Execute script as a global program
RUN ln -s /app/main.py /usr/local/bin/ntcount
RUN chmod +x /usr/local/bin/ntcount

# Startup script
ENTRYPOINT ["sh", "/docker/startup.sh"]
