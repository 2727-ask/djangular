#!/bin/sh

ssh root@64.227.176.176 <<EOF
  cd projectdir
  source env/bin/activate
  cd djangular
  git add .
  git commit -m "Server Commit Made"
  git pull origin main
  pip install -r requirements.txt
  ./manage.py migrate
  sudo supervisorctl restart djangular
  exit
EOF