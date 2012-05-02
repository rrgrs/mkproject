settings = {}

settings['reg'] = '''DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

ADMINS = (
	('', ''),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = '%(p_name)s'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = None

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

# Fixtures
FIXTURES_DIR = join(TRUNK_DIR, 'fixtures')

# Media
MEDIA_ROOT = join(TRUNK_DIR, 'media')

# Static paths, These will contain website's static files, such as
# .js, .css, images and others. The STATIC_ROOT is only good for serving
# the debug static server, cause this path will be served by the web servah
STATIC_ROOT = join(TRUNK_DIR, 'static')
STATIC_URL = '/static/'

# Media URL
MEDIA_URL = HTTPS_MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = '%(key)s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
	'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
	#'django.middleware.gzip.GZipMiddleware',
	#'django.middleware.common.CommonMiddleware',
	#'django.contrib.sessions.middleware.SessionMiddleware',
	#'django.contrib.auth.middleware.AuthenticationMiddleware',
	#'django.middleware.transaction.TransactionMiddleware',
	#'django.contrib.messages.middleware.MessageMiddleware',
	#'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	#'django.middleware.csrf.CsrfViewMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	#'django.core.context_processors.auth',
	#'django.core.context_processors.request',
	#'django.core.context_processors.i18n',
	#'django.contrib.messages.context_processors.messages',
	#'common.context_processors.paths',
)
	
ROOT_URLCONF = '%(p_name)s.urls'

TEMPLATE_DIRS = (
	join(TRUNK_DIR, 'templates')
)

INSTALLED_APPS = (
	# Django
	#'django.contrib.auth',
	#'django.contrib.contenttypes',
	#'django.contrib.sessions',
	#'django.contrib.sites',
	#'django.contrib.admin',
	#'django.contrib.sitemaps',
	#'django.contrib.flatpages',
	#'django.contrib.messages',
	#'django.contrib.comments', 

	# Deps

	# Apps

)


#MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

#AUTH_PROFILE_MODULE = ''

#EMAIL_HOST = ''
#SERVER_EMAIL = DEFAULT_FROM_EMAIL = '' 
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_PORT = 25

#LOGIN_URL = '''''

settings['production'] = '''from settings import *

DEBUG = TEMPLATE_DEBUG = False

#STATIC_URL = ''
#MEDIA_URL = ''


DATABASE_NAME = '%(p_name)s_production'
DATABASE_USER = ''
DATABASE_PASSWORD = ''

# Force SSL Settings
#HTTPS_SUPPORT = True
#SECURE_PATHS = (
#)'''

settings['staging'] = '''from settings import *

DEBUG = TEMPLATE_DEBUG = False

#STATIC_URL = ''
#MEDIA_URL = ''


DATABASE_NAME = '%(p_name)s_staging'
DATABASE_USER = ''
DATABASE_PASSWORD = ''

# Force SSL Settings
#HTTPS_SUPPORT = True
#SECURE_PATHS = (
#)'''


urls = '''from django.conf.urls.defaults import patterns, include, handler404, handler500
from django.contrib import admin
from django.conf import settings

admin.autodiscover()
urlpatterns = patterns('',
    (r'^$', include('')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT}),
    )
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
#urlpatterns += patterns('',
#    (r'^', include('django.contrib.flatpages.urls')),
)'''


manage = '''#!/usr/bin/env python

from warnings import filterwarnings
import MySQLdb
filterwarnings('ignore', category=MySQLdb.Warning)

try:
    import settings # Assumed to be in the same directory.
    import sys
    from os.path import join
    sys.path[0:0] = [
        join(settings.TRUNK_DIR, 'apps'),
        join(settings.TRUNK_DIR, 'deps'),
        ]
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\
You'll have to run django-admin.py, passing it your settings module. \
(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\
" % __file__)
    sys.exit(1)


from django.core.management import execute_manager

if __name__ == "__main__":
    execute_manager(settings)'''
    
apache = {}

apache['production'] = '''import sys, os
from os.path import dirname, join, realpath


sys.path[0:0] = [
    realpath(join(dirname(__file__), '..', 'apps')),
    realpath(join(dirname(__file__), '..', 'deps')),
    realpath(join(dirname(__file__), '..', '%(p_name)s')),
    realpath(join(dirname(__file__), '..')),
]

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.production'
os.environ['PYTHON_EGG_CACHE'] = realpath(join(dirname(__file__), '..', '..', '.cache'))
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()'''


apache['staging'] = '''import sys, os
from os.path import dirname, join, realpath


sys.path[0:0] = [
    realpath(join(dirname(__file__), '..', 'apps')),
    realpath(join(dirname(__file__), '..', 'deps')),
    realpath(join(dirname(__file__), '..', '%(p_name)s')),
    realpath(join(dirname(__file__), '..')),
]

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.staging'
os.environ['PYTHON_EGG_CACHE'] = realpath(join(dirname(__file__), '..', '..', '.cache'))
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()'''
