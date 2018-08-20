#!/usr/bin/env bash
# This script will prepare our webservers for deployment

# first update + install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# create folders if not already existent
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# create a fake html page
echo -e "<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n
</html>" | sudo tee /data/web_static/releases/test/index.html

# now create a symbolic link for current linked to releases/test
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# now change ownership of folder /data/ to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# lastly create an alias and update the nginx configuration
sudo sed -i "35i location /hbnb_static {\nalias /data/web_static/current/;\n}" /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart
