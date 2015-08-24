"""
Django settings for madlibs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #heroku setting?


# Secret key and other settings are stored in heroku config vars
# See README.md for details and install steps

SECRET_KEY = '^=4srp3k_ec0-=d7zb0t+s&&vlhv#r_eaha%ti6*7&5!!ajmrk' 
#SECRET_KEY = os.environ['MADLIBS_SECRET_KEY']

DEBUG = True
#DEBUG = os.environ['MADLIBS_DEBUG']

TEMPLATE_DEBUG = True
#TEMPLATE_DEBUG = os.environ['MADLIBS_TEMPLATE_DEBUG']

# Allow all host headers
#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stories',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'madlibs.urls'

WSGI_APPLICATION = 'madlibs.wsgi.application'


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago' #was UTC by default

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Heroku Host Settings

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, 'madlibs/static'),
    os.path.join(BASE_DIR, 'static'),  #heroku setting?
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



# Database
# Parse database configuration from $DATABASE_URL
import dj_database_url

# if 'DATABASE_URL' does no exist, then it's local machine
if not os.environ.has_key('DATABASE_URL'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'madlibs',
            'USER': 'muser',
            'PASSWORD': 'mpass',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')