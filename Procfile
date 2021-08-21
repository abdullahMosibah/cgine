release: python manage.py migrate

web: gunicorn --timeout 30 config.wsgi:application
