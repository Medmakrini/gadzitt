"""
Django settings for gadzIt project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
from django.utils.translation import gettext 
from django.utils.translation import gettext_lazy , pgettext
django.utils.translation.ugettext = gettext
django.utils.translation.ugettext_lazy = gettext_lazy

from django.dispatch import Signal

token_issued = Signal(['request', 'user'])
token_refreshed = Signal(['request', 'user'])


#from django.dispatch import Signal as S
#django.dispatch.Signal=S



import django_heroku
from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w7n8)g73h57m835ft@u=sn8rku$ajrfsuitx%-)3nr4msswh(l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['gadzit.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'FormationForm',
    'multiselectfield',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'graphql_auth',
    'django_filters',
    'corsheaders'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
 ]



CORS_ORIGIN_ALLOW_ALL = True


CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://gadzit.herokuapp.com',
    'http://localhost:3000',
    'https://gadzit.herokuapp.com'
    ]

CORS_ORIGIN_WHITELIST = [ 
    'http://192.168.1.63:8000',
    'http://10.0.1.1:8081',
    'http://192.168.1.63:3000',
    'http://localhost:3000',
    'http://192.168.1.63:3000',
    'http://localhost:8000'
]

ROOT_URLCONF = 'gadzIt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gadzIt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9mo6cmlgq839f',
        'USER': 'ctxpavamqordje',
        'PASSWORD':'1a197feaf97671b522653a92160bd7e77a241ab95d27c3ab85b7f46309cbffb1',
        'HOST': 'ec2-54-91-223-99.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

#STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.ExtendUser'

GRAPHENE = {
    'SCHEMA' : 'users.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
        "graphql_jwt.middleware.JSONWebTokenMiddleware",

    ],
}

AUTHENTICATION_BACKENDS = [
    'graphql_auth.backends.GraphQLAuthBackend',
    'django.contrib.auth.backends.ModelBackend',  # important to have this as well.
]

GRAPHQL_JWT = {
    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ObtainJSONWebToken",
      
    ],
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": timedelta(hours=12),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
    "JWT_ALLOW_ARGUMENT": True,



}


GRAPHQL_AUTH = {
    'JWT_ALLOW_ARGUMENT': True,
    "ALLOW_LOGIN_NOT_VERIFIED": False,
    'REGISTER_MUTATION_FIELDS': {
        'email': 'String',
        'username':'String',
        'phone': 'String',
        'first_name': 'String',
        'last_name': 'String',
        'cell': 'String',
        'day': 'String',
        'year': 'String',
        'psw': 'String',
        
        
    },
    

    'UPDATE_MUTATION_FIELDS': {
        'phone': 'String',
        'year': 'String',
        'cell': 'String',
        'day': 'String',
        'psw': 'String',

    }
}


PASSWORD_HASHERS = [
  'django.contrib.auth.hashers.PBKDF2PasswordHasher',
  'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
  'django.contrib.auth.hashers.Argon2PasswordHasher',
  'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
  'django.contrib.auth.hashers.BCryptPasswordHasher',
  'django.contrib.auth.hashers.SHA1PasswordHasher',
  'django.contrib.auth.hashers.MD5PasswordHasher',
  'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
  'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
  'django.contrib.auth.hashers.CryptPasswordHasher',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

django_heroku.settings(locals())
