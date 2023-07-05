#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static
apt-get -y update
apt-get -y upgrade

# Installs Nginx
apt-get -y install nginx

# Creates the folders for the deployment of web_static
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Creates a fake HTML file
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html

# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Gives ownership of the /data/ folder to the ubuntu user and group
chown -hR ubuntu:ubuntu /data/

# Updating the Nginx configuration to serve the content of /data/web_static/current/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restarting Nginx after applying changes
service nginx start
