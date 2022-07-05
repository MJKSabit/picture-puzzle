"""
Django settings for CSE_FEST_2022_Picture_Puzzle project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

dot_env_path = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dot_env_path):
    from dotenv import load_dotenv

    load_dotenv(dot_env_path)

"""-------------------------------------------------- env variables start -----------------------------------------"""
SERVER = True
DEBUG = not SERVER
SECRET_KEY = "h^z13$qr_s_wd65@gnj7a=xs7t05$w7q8!x_8zsld#"

CONTEST_STARTED = True
CONTEST_ENDED = False


SHOW_MEME = True
SHOW_HACK = True


SHOMOBAY_SHOMITI = True
SHOW_SHOMITI = True
MEAN = 0.5
DEVIATION = 2
SPREAD = 60
SCALE = 0.9
TRANSITION00 = 0.8     # -cheat(t+1)|-cheat(t)
TRANSITION01 = 0.1     # -cheat(t+1)|+cheat(t)
TRANSITION10 = 0.2     # +cheat(t+1)|-cheat(t)
TRANSITION11 = 0.9     # +cheat(t+1)|+cheat(t)
EMISSION00 = 0.6       # +time(t)|-cheat(t)
EMISSION01 = 0.4       # -time(t)|-cheat(t)
THRESHOLD = 0.7
START_PROB = 0.2

LEADERBOARD_PAGE = 10
MEME_WRONG = 5

"""-------------------------------------------------- env variables end -------------------------------------------"""
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'contest_arena',
    'shomobay_shomiti_detector',
    'crispy_forms',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CSE_FEST_2022_Picture_Puzzle.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'CSE_FEST_2022_Picture_Puzzle.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if SERVER:
    DATABASES = {
        'default': {
            'ENGINE': 'mysql.connector.django',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASS'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT')
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Extra places for collectstatic to find assets files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
