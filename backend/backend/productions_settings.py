import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'kji3n2zdjud7#$ovbvs0+_c3br8va@vuin!*lqfo%w^7nwektv'

DEBUG = False

ALLOWED_HOSTS = [os.getenv('HOSTS')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),  # data base name
        'USER': os.getenv('DB_USER_NAME'),
        'PASSWORD': os.getenv('DB_USER_PASSWORD'),
        'HOST': 'localhost',
        'PORT': os.getenv('DB_PORT'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_DIR = os.path.join(BASE_DIR, "static")
