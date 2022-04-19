from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangularprod',
        'USER': 'ashutoshkumbhar',
        'PASSWORD': 'Asdfghjkl@27',
        'PORT': '5432',
    }
}

# sudo -u root psql postgres