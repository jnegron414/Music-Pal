import os

from .universal_settings import *

DEBUG = True
ENVIRONMENT = "local"

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'root',
        'PASSWORD': 'rootpassword',
        'HOST': 'db',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = 'temp/static'

# Media files
MEDIA_ROOT = "tmp/media"
MEDIA_URL = "/media"

SECRET_KEY = '^!0mlye2%tb@p(w8th0g@6rswfmoj*+2_%b*hucplmuq0^8o8w'

ENABLE_REDIS_CACHEOPS = False  # TODO
REDIS_CACHE_TIMEOUT = 60 * 60
REDIS_HOST = 'redis-cache'

# Sentry Settings
ENABLE_SENTRY = False
SENTRY_PUBLIC_KEY = ''
SENTRY_PROJCT_ID = ''
SENTRY_DSN = 'https://%s@sentry.io/%s' % (SENTRY_PUBLIC_KEY, SENTRY_PROJCT_ID)

# Spotify Settings
SPOTIFY_CLIENT_ID = ''
SPOTIFY_CLIENT_SECRET = ''
