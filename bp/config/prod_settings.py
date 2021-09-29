import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-+9_asrz-rrx-ozd49moydb78-hjedrl)&-qv_h$#bdg+9h)u9*'

DEBUG = False

ALLOWED_HOSTS = ['bp.grodno.belpost.by', '172.16.190.221', 'localhost', '127.0.0.1']

DATABASES = {
    '_default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default': {
        # 'ENGINE': 'django.db.backends.oracle',
        'ENGINE': 'extensions.oracle',
        'NAME': 'ORCL',
        'USER': 'WWW',
        'PASSWORD': 'www_dba',
        'HOST': '172.16.188.140',
        'PORT': '1521',
        # Сколько секунд удерживать соединение с БД
        "CONN_MAX_AGE": 10
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

EMAIL_HOST = '172.16.190.190'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = "no_reply@belpost.by"
