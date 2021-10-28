from pathlib import Path

from config.settings import get_env

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['bp.belpost.by', '172.16.100.227', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'extensions.oracle',
        'NAME': 'ORCL',
        'USER': 'WWW',
        'PASSWORD': get_env('DATABASE_DEF_PASS'),
        'HOST': '172.16.188.140',
        'PORT': '1521',
        # Сколько секунд удерживать соединение с БД
        "CONN_MAX_AGE": 10
    },
    'ref': {
        'ENGINE': 'extensions.oracle',
        'NAME': 'ORCL',
        'USER': 'REF',
        'PASSWORD': get_env('DATABASE_REF_PASS'),
        'HOST': '172.16.188.140',
        'PORT': '1521',
        # Сколько секунд удерживать соединение с БД
        "CONN_MAX_AGE": 10
    },
    'nsi': {
        'ENGINE': 'extensions.oracle',
        'NAME': 'ORCL',
        'USER': 'NSI',
        'PASSWORD': get_env('DATABASE_NSI_PASS'),
        'HOST': '172.16.188.140',
        'PORT': '1521',
        # Сколько секунд удерживать соединение с БД
        "CONN_MAX_AGE": 10
    },
    'ptks': {
        'ENGINE': 'extensions.oracle',
        'NAME': 'tracksys',
        'USER': 'TRACKSYS_VIEW',
        'PASSWORD': get_env('DATABASE_PTKS_PASS'),
        'HOST': '172.16.100.24',
        'PORT': '1521',
        # Сколько секунд удерживать соединение с БД
        "CONN_MAX_AGE": 10
    },
    '_default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

# Кеширование
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'PASSWORD': get_env('REDIS_PASS'),
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'select2': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'TIMEOUT': 3000,
        'OPTIONS': {
            'PASSWORD': get_env('REDIS_PASS'),
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {   # Схожесть пароля и набора атрибутов пользователя
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'user_attributes': 'username',
            'max_similarity': 0.7,
        }
    },
    {   # Минимальная длинна пароля
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {   # Проверяет, не является ли пароль обычным паролем из списка 20 000 вариантов
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    # {   # Проверяет, является ли пароль не полностью числовым
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]
