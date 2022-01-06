#Grab the latest alpine image
FROM heroku/heroku:20-build

# Install python and pip
RUN apt -y update
RUN apt-get -y install python3 bash python3-pip
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt
RUN useradd -m myuser
USER myuser
# Add our code
ADD ./ /opt/graphapp
WORKDIR /opt/graphapp
ENV heroku config

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT main:app
#CMD gunicorn main:app --host 0.0.0.0 --port $PORT