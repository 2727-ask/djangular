#!/bin/sh

ssh root@64.227.176.176 <<EOF
  cd projectdir
  source env/bin/activate
  cd djangular
  git pull
  pip install -r requirements.txt
  ./manage.py migrate
  sudo supervisorctl restart djangular
  exit
EOF