covidtracker
============

Tracking Covid Cases

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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

6. Run the server:
```shell
python manage.py runserver 0.0.0.0:8000
```

7. Git commands
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
## Field Description

### Location

- **location_code**: Unique code for each row entry.
	For example Brussels-Belgium: 5602, East Flanders-Belgium: 5603
- **country_code**: Unique code for each country
	For example Belgium: 56
- **iso2** and **iso3**: Country code identifiers
- **fibs**:  Federal Information Processing Standards code, USA only.
- **province_state**: Province/State
- **country_region**: Country/Region
- **location_name**: Country name and the location name together. For example Antwerp, Belgium
- **slug**: Unique slug for each location. Generated with location_name if it is not provided.
- **country_population**
- **latitude**
- **longitute**
