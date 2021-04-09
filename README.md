covidtracker
============

Tracking Covid Cases

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

## Requirements
- Django 3
- Django Rest Framework
- PostgreSQL

## Getting Up and Running Locally

1. Create a virtualenv and activate it:
```shell
virtualenv -p  python3.8 venv

source venv/bin/activate
```

2. Install development requirements:
```shell
pip install -r requirements/local.txt
```
3. Create a new PostgreSQL database using createdb:
```shell
createdb <database name> -U postgres --password <password>
```
4. Set the environment variables:
```shell
export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/<DB name given to createdb>

export CELERY_BROKER_URL=redis://localhost:6379/0

export USE_DOCKER=no
```

5. Apply migrations:
```shell
python manage.py migrate
```
6. Run the server
```shell
python manage.py runserver 0.0.0.0:8000
```

7. Git
```shell
git init

pre-commit install
```
## Getting Up and Running Locally With Docker

You should have Docker and Docker Compose installed in your system.

### To build the stack
```shell
docker-compose -f local.yml build
```

### To run the stack

```shell
docker-compose -f local.yml up

docker-compose up
```
### To execute Django commands

```shell
docker-compose -f local.yml run --rm django python manage.py migrate

docker-compose -f local.yml run --rm django python manage.py createsuperuser
```
