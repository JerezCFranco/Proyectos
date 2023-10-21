from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'blogdb',
        'USER' : "root",
        'PASSWORD' : "carlitos1",
        'HOST' : 'localhost',
        'PORT' : 3306,
    }
}