#Grab the latest alpine image
FROM heroku/heroku:20-build

# Install python and pip
RUN apt -y update
RUN apt-get -y install python3 bash python3-pip
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD ./app_here /opt/webapp
WORKDIR ./app_here

# Expose is NOT supported by Heroku
# EXPOSE 5000

# Run the image as a non-root user
#RUN adduser -D endpointuser
#USER endpointuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
#CMD uvicorn --bind 0.0.0.0:$PORT wsgi
CMD uvicorn --app-dir /opt webapp:app --host 0.0.0.0 --port $PORT