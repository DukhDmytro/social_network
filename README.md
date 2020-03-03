# Social Network

Object of this task is to create a simple REST API. You have to use Django and
Django rest framework.

## Getting Started
1. Install requirements

`pip install -r requirements.txt`

2. Database settings

Edit social_network/personal_settings.py 

### Postgres
`DATABASES_ = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'user_name',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}`
### SQLite
`DATABASES_ = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'),
    }
}`

### Other settings
`SECRET_KEY_ = 'Your_key'`

`HUNTER_API_KEY_ = 'Your_key'`

### Migrations
`python manage.py makemigrations`

`python manage.py migrate`

### Start project

`python manage.py runserver`

### Running the tests
`python manage.py test`

## REST API endpoints
Api documentation
`/api/swagger`

`api/users/`

`api/login/`

`api/login/refresh/`

`api/posts/`

`api/posts/<slug>/`

`api/posts/<slug>/like/`

`api/posts/<slug>/unlike/`

`/api/chat/`

## Built With
[Django](https://www.djangoproject.com/)

[Django Rest Framevork](https://www.django-rest-framework.org/)

[Django JWT](https://github.com/davesque/django-rest-framework-simplejwt)

[Emailhunter](https://github.com/VonStruddle/PyHunter)
