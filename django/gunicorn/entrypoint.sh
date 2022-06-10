#!/bin/sh
set -eu

# WORKDIR
cd /opt/app

# adminユーザー
email=root@localhost
user=admin
pass=admin

# initialize db
if [ ! -e db.sqlite3 ]; then
  python manage.py migrate
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$user', '$email', '$pass')"| python manage.py shell
fi

# update db
#python manage.py makemigrations
python manage.py migrate

# update static files
python manage.py collectstatic --no-input

# run
gunicorn mysite.wsgi --reload --bind=0.0.0.0:8000
