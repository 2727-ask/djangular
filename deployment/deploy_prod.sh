#!/bin/sh

ssh root@64.227.176.176 <<EOF
  cd projectdir/djangular
  git pull
  source env/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  sudo supervisorctl restart djangular
  exit
EOF