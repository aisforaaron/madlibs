#!/bin/bash
# Bash script to run extra Madlibs install steps after Ansible
echo "This script will activate a virtualenv, create a super user, and start the python server."

cd /vagrant_data/mproj

source venv/bin/activate

echo "Setup new admin user? y/n:"
read SETUPUSER

if [ $SETUPUSER = 'y' ]; then

  echo "The password prompt is for django admin user. Enter 'admin' twice:"
  python manage.py createsuperuser --username=admin --email=admin@localhost 

fi

#- if data wasn't loaded (it should be)
#    $ python manage.py loaddata stories/fixtures/stories.yaml

echo "After the runserver starts, you can open the url in a browser"
echo "http://192.168.33.53:8000"
python manage.py runserver 0.0.0.0:8000