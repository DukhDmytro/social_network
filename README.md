# Social Network

Object of this task is to create a simple REST API. You have to use Django and
Django rest framework.

## Getting Started
1. Install requirements

`pip install -r requirements.txt`

2. Database settings

Edit social_network/personal_settings.py 

`SECRET_KEY_ = 'Your_key'`

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
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}`

`HUNTER_API_KEY_ = 'Your_key'`

### Migrations
`python manage.py makemigrations`

`python manage.py migrate`

### Start project

`python manage.py runserver`

### Running the tests
`python manage.py test`

## REST API endpoints

`api/signin`

`api/login`

`api/login/refresh`

`api/post`

`api/post/<slug>`

`api/post/like/<slug>`

`api/post/unlike/<slug>`

## Built With
[Django](https://www.djangoproject.com/)

[Django Rest Framevork](https://www.django-rest-framework.org/)

[Django JWT](https://github.com/davesque/django-rest-framework-simplejwt)

[Emailhunter](https://github.com/VonStruddle/PyHunter)