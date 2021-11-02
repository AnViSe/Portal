import os
from pathlib import Path
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = str(os.environ.get('DEBUG', 'False')) == 'True'

# Application definition
PROJECT_NAME = os.environ.get('PROJECT_NAME')
PROJECT_DOMAIN = os.environ.get('PROJECT_DOMAIN')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'rest_framework_datatables',
    'django_filters',
    'django_select2',

    'allauth',
    'allauth.account',
    'widget_tweaks',
    'mptt',
    'maintenancemode',
    'crispy_forms',

    'core',
    'apps.welcome',
    'apps.home',
    'apps.account',
    'apps.references',
    'apps.modules',
    'apps.modules.delivery',
]

AUTH_USER_MODEL = 'apps_account.CustomUser'

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# MIDDLEWARE_CLASSES = [
#      'django.middleware.locale.LocaleMiddleware',
# ]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath('templates'),
            BASE_DIR.joinpath('apps/account/templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = ['core/locale']

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath('static')
STATICFILES_DIRS = [
    BASE_DIR.joinpath('config/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATE_FORMAT = '%d.%m.%Y'
DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
DATE_INPUT_FORMATS = ['%d.%m.%Y']
DATETIME_INPUT_FORMATS = ['%d.%m.%Y %H:%M:%S']

SITE_ID = 1

# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 50,
    'DATE_FORMAT': DATE_FORMAT,
    'DATETIME_FORMAT': DATETIME_FORMAT,
    'DATE_INPUT_FORMATS': DATE_INPUT_FORMATS,
    'DATETIME_INPUT_FORMATS': DATETIME_INPUT_FORMATS
}

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Tell select2 which cache configuration to use:
SELECT2_CACHE_BACKEND = "select2"
SELECT2_CSS = ('/static/css/select2/select2.css',
               '/static/css/select2/select2-bootstrap4.css',)
SELECT2_JS = ('/static/js/select2/select2.full.js',)
SELECT2_I18N_PATH = '/static/js/select2/i18n'
# SELECT2_I18N_AVAILABLE_LANGUAGES = ('ru',)

# Укажите используемый метод входа ("username" | "email" | "username_email")
ACCOUNT_AUTHENTICATION_METHOD = "username"

# При регистрации от пользователя требуется указать адрес электронной почты.
# ACCOUNT_EMAIL_REQUIRED = True

# Количество дней для подтверждения регистрации по электронной почте
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 5

# Метод проверки электронной почты при регистрации: "mandatory", "optional", or "none"
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# URL-адрес для перенаправления после успешного подтверждения по электронной почте,
# если пользователь не вошел в систему.
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL

# URL-адрес для перенаправления после успешного подтверждения по электронной почте
# в случае аутентифицированного пользователя.
# Установите None для использования settings.LOGIN_REDIRECT_URL.
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

# Период восстановления (в секундах) после отправки электронного письма с подтверждением,
# в течение которого дальнейшие электронные письма не отправляются.
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 180

# Определяет, должны ли пользователи подтверждать адрес вручную
# ACCOUNT_CONFIRM_EMAIL_ON_GET = False

# Количество неудачных попыток входа
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

# Продолжительность запрета попыток входа пользователя с момента последней неудачной попытки входа
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

# Автоматический вход пользователя в систему после подтверждения своего адреса электронной почты.
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# Автоматический вход пользователя в систему после сброса пароля
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False

# Автоматический выход из системы после изменения или установки пароля
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False

# Отключить запрос подтверждения выхода
ACCOUNT_LOGOUT_ON_GET = True

# Установить ссылку перехода после выхода из системы
# ACCOUNT_LOGOUT_REDIRECT_URL = "home"

# Контролирует время жизни сеанса.
# Установите, чтобы None спрашивать пользователя («Запомнить меня?»),
# False Не помнить и True всегда помнить.
ACCOUNT_SESSION_REMEMBER = None

# Нужно ли пользователю дважды вводить адрес электронной почты при регистрации
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False

# Требуется ли пользователю дважды вводить пароль при регистрации
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# URL-адрес (или имя URL-адреса) для перенаправления сразу после регистрации.
# ACCOUNT_SIGNUP_REDIRECT_URL = LOGIN_REDIRECT_URL

# Список имен пользователей, которые пользователи не могут использовать
ACCOUNT_USERNAME_BLACKLIST = ['admin, Admin', 'administrator', 'Administrator']

# Уникальность адресов электронной почты
ACCOUNT_UNIQUE_EMAIL = True

# Минимальная длина имени пользователя
ACCOUNT_USERNAME_MIN_LENGTH = 3

MAINTENANCE_503_TEMPLATE = 'errors/503.html'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# PHONENUMBER_DEFAULT_REGION = 'BY'
# PHONENUMBER_DEFAULT_FORMAT = 'E164'

# Для переопределения меток в сообщениях
MESSAGE_TAGS = {
    messages.INFO: 'alert-info',
    messages.DEBUG: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.ERROR: 'alert-danger',
    messages.WARNING: 'alert-warning',
}

# MPTT
# Сдвиг веток в дереве (пиксели)
MPTT_ADMIN_LEVEL_INDENT = 20

DEFAULT_AVATAR_URL = ''

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *

if DEBUG:
    INTERNAL_IPS = ['127.0.0.1', '172.16.190.61', ]
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
