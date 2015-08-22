"""
Django settings for madlibs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Secret key and other settings are stored in heroku config vars
# See README.md for details and install steps
SECRET_KEY = os.environ['MADLIBS_SECRET_KEY']
DEBUG = os.environ['MADLIBS_DEBUG']
TEMPLATE_DEBUG = os.environ['MADLIBS_TEMPLATE_DEBUG']
ALLOWED_HOSTS = []


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


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

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

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago' #was UTC by default

USE_I18N = True

USE_L10N = True

USE_TZ = True




# HEROKU SETTINGS THAT WORK ----------------------- ///

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# also https://devcenter.heroku.com/articles/django-assets

STATIC_URL = '/static/'

# exmaple: STATIC_ROOT = '/vagrant_data/pydev.local/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    # why is this madlibs/static not just static?
    os.path.join(BASE_DIR, 'madlibs/static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
