import os

ALLOWED_HOSTS = ['bp.belpost.by', '172.16.100.227', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'extensions.oracle',
        'NAME': os.environ.get('DATABASE_DEF_NAME'),
        'USER': os.environ.get('DATABASE_DEF_USER'),
        'PASSWORD': os.environ.get('DATABASE_DEF_PASS'),
        'HOST': os.environ.get('DATABASE_DEF_HOST'),
        'PORT': int(os.environ.get('DATABASE_DEF_PORT')),
        # Сколько секунд удерживать соединение с БД
        'CONN_MAX_AGE': 60,
        'OPTIONS': {
            'threaded': True,
        },
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

# Кеширование
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_LOCATION') + '/1',
        'OPTIONS': {
            'PASSWORD': os.environ.get('REDIS_PASS'),
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'select2': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_LOCATION') + '/2',
        'TIMEOUT': 3000,
        'OPTIONS': {
            'PASSWORD': os.environ.get('REDIS_PASS'),
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_LOCATION') + '/3',
        'OPTIONS': {
            'PASSWORD': os.environ.get('REDIS_PASS'),
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    },
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
