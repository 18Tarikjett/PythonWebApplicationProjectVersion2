#!/bin/bash
set -eiou pipefail
sleep 10
python manage.py migrate
python manage.py createsuperuser --noinput 
python manage.py runserver 0.0.0.0:8000
python manage.py check --deploy