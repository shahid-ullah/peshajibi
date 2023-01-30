## Basic startup template for django project.

## Features Included

- custom user model
- separate requirements file for production and development
- app configurations: django debug toolbar, django extensions, django environ, whitenoise
- media files, static files configurations
- multiple database connection based on environment variable(default: sqlite)

## Basic setup

```sh
$ git clone git@github.com:shahid-ullah/django_base_app.git
$ cd django_base_app
$ virtualenv .venv
$ source .venv/bin/activate
$ touch .env
$ cp .env.dist .env
$ cd requirements
$ pip-compile --output-file requirements.txt.dev requirements.in.production requirements.in.dev
$ cd ..
$ python manage.py runserver
```
