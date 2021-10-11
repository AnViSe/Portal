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

# Кеширование
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            # 'PASSWORD': 'XXXXXXXXXXX',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'select2': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'TIMEOUT': 3000,
        'OPTIONS': {
            # 'PASSWORD': 'XXXXXXXXXXX',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
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

EMAIL_HOST = '172.16.190.190'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = "no_reply@belpost.by"
