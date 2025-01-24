#!/bin/sh
makemigrations.sh --noinput
echo 'Executando migrate.sh' 
python manage.py migrate --noinput
