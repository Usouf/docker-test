#!/bin/bash

/usr/local/bin/python manage.py migrate --noinput

/usr/local/bin/python manage.py elpsuperuser

/usr/local/bin/python manage.py collectstatic --noinput

RUN_PORT=${PORT:-8000}
/usr/local/bin/gunicorn elp.wsgi:application --bind "0.0.0.0:${RUN_PORT}"
