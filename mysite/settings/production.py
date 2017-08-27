from .base import *

DEBUG = False

# ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', '.mywaterbuffalo.com')]


# Use the cached template loader so template is compiled once and read from
# memory instead of reading from disk on each load.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

# CORS_ORIGIN_WHITELIST: specify a list of origin hostnames that are authorized to make a cross-site HTTP request
# CORS_ORIGIN_WHITELIST = (
# )

# CORS_ORIGIN_ALLOW_ALL: if True, the whitelist will not be used and all origins will be accepted
CORS_ORIGIN_ALLOW_ALL = True
