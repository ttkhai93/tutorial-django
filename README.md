## Run (Development environment only)
- python manage.py runserver

## Run (Production environment)
- gunicorn mysite.wsgi

## Make migrations
- python manage.py makemigrations [polls]

## Prints SQL scripts to terminal
- python manage.py sqlmigrate polls 0001

## Run all migrations that haven’t been applied
- python manage.py migrate

## Run tests
- python manage.py test [polls]

## Check coverage
- coverage run --source='.' manage.py test [polls]
- coverage report