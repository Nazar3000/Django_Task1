import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {

'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'django_task1db',

        'USER': 'django_task1',

        'PASSWORD': 'Qwerty!123',

        'HOST': 'localhost',

        'PORT': '',

    }


}