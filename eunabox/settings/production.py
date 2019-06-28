from .base import *
import dj_database_url
import django_cache_url

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'eunabox.com']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

BASE_URL = 'http://localhost:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

CACHES = {'default': django_cache_url.config()}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

try:
    from .local import *
except ImportError:
    pass
