# Заполнить и сохранить как: local_settings.py
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    '_default': {
        'ENGINE': 'extensions.oracle',
        'NAME': os.environ.get('DATABASE_DEF_NAME'),
        'USER': os.environ.get('DATABASE_DEF_USER'),
        'PASSWORD': os.environ.get('DATABASE_DEF_PASS'),
        'HOST': os.environ.get('DATABASE_DEF_HOST'),
        'PORT': int(os.environ.get('DATABASE_DEF_PORT')),
        # Сколько секунд удерживать соединение с БД
        'CONN_MAX_AGE': 60,
        'TIME_ZONE': 'Europe/Minsk',
    },
    'ref': {
        'ENGINE': 'extensions.oracle',
        'NAME': os.environ.get('DATABASE_REF_NAME'),
        'USER': os.environ.get('DATABASE_REf_USER'),
        'PASSWORD': os.environ.get('DATABASE_REF_PASS'),
        'HOST': os.environ.get('DATABASE_REF_HOST'),
        'PORT': int(os.environ.get('DATABASE_REF_PORT')),
        # Сколько секунд удерживать соединение с БД
        'CONN_MAX_AGE': 10
    },
    'nsi': {
        'ENGINE': 'extensions.oracle',
        'NAME': os.environ.get('DATABASE_NSI_NAME'),
        'USER': os.environ.get('DATABASE_NSI_USER'),
        'PASSWORD': os.environ.get('DATABASE_NSI_PASS'),
        'HOST': os.environ.get('DATABASE_NSI_HOST'),
        'PORT': int(os.environ.get('DATABASE_NSI_PORT')),
        # Сколько секунд удерживать соединение с БД
        'CONN_MAX_AGE': 10
    },
    'ptks': {
        'ENGINE': 'extensions.oracle',
        'NAME': os.environ.get('DATABASE_PTKS_NAME'),
        'USER': os.environ.get('DATABASE_PTKS_USER'),
        'PASSWORD': os.environ.get('DATABASE_PTKS_PASS'),
        'HOST': os.environ.get('DATABASE_PTKS_HOST'),
        'PORT': int(os.environ.get('DATABASE_PTKS_PORT')),
        # Сколько секунд удерживать соединение с БД
        'CONN_MAX_AGE': 10
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR.joinpath('cache'),
    },
    'select2': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR.joinpath('select2'),
    },
    'session': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR.joinpath('session'),
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        },
    },
]
