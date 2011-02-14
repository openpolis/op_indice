# Django settings for op_indice project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'NAME': 'op_indice.db',
        'ENGINE': 'django.db.backends.sqlite3',
    },
    'opp': {
        'NAME': 'op_openparlamento',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'selector',
        'PASSWORD': ''
    },
    'op': {
        'NAME': 'op_openpolis',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'selector',
        'PASSWORD': ''
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'it-IT'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ta(f+=2nf[rk094+4kflkj09dcu094j+#0=?^riokfmfu=$okf'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
#    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'middleware.SQLLogToConsoleMiddleware',
)

ROOT_URLCONF = 'op_indice.urls'

TEMPLATE_DIRS = (
  "/Users/guglielmo/Workspace/op_indice/templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'south',
    'django_extensions',
    'charts',
)

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
#CACHE_MIDDLEWARE_SECONDS = 300
#CACHE_MIDDLEWARE_KEY_PREIX = 'op_indice'
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

OPENPARLAMENTO_URL = 'http://parlamento.openpolis.it'
FETCH_S3_IMAGES = True