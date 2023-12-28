#!/bin/bash

/usr/local/bin/python manage.py makemigrations --noinput
/usr/local/bin/python manage.py migrate --noinput
/usr/local/bin/python manage.py collectstatic --noinput

/usr/local/bin/celery -A your_project_name worker -l info &
/usr/local/bin/celery -A your_project_name beat -l info &

RUN_PORT=${PORT:-8000}
/usr/local/bin/gunicorn docker_test.wsgi:application --bind "0.0.0.0:${RUN_PORT}"
