"""
Django settings for coldlands project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""


# Local settings
try:
    from coldlands.settings import *
    print "[INFO] Global settings imported."
except:
    print "[ERROR] Can't import global settings!!!"

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h!tuv!7*j*y)-tmmdhx$*(4d$n1-ee$ch@edv*cqs=-19_sb0%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS.extend([
])


# MIDDLEWARE_CLASSES.insert(0,'django_hosts.middleware.HostsRequestMiddleware')
MIDDLEWARE_CLASSES.extend([
])
# MIDDLEWARE_CLASSES.append('django_hosts.middleware.HostsResponseMiddleware')

#ROOT_HOSTCONF = 'coldlands.hosts'
#DEFAULT_HOST = 'main'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'coldlands',
        'USER': 'cluser',
        'PASSWORD': 'clpassword',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'ilya.zolotko@yahoo.com'
EMAIL_HOST_USER = 'ilya.zolotko@gmail.com'
EMAIL_HOST_PASSWORD = 'north carolina'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_SSL_CERTFILE =
# EMAIL_SSL_KEYFILE =
EMAIL_HOST = 'smpt.gmail.com'
EMAIL_PORT = 587

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/