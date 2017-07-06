FROM alpine:3.6

MAINTAINER Lukasz Dynowski ludd@bioinformatics.dtu.dk

# Copy app dir form host into image
COPY ./app /app
WORKDIR /app

# OS Update & Upgrade
RUN apk update && apk upgrade

# Install packages
RUN apk add \
  python \
  py-pip

# Install application wide packages
RUN pip install -r requirements.txt

# Execute script as a global program
RUN ln -s /app/main.py /usr/local/bin/ntcounter
RUN chmod +x /usr/local/bin/ntcounter

# Startup script
#CMD ["sh", "/app/scripts/startup.sh"]
