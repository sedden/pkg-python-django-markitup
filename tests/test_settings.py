from os.path import dirname, join
MIU_TEST_ROOT = dirname(__file__)

INSTALLED_APPS = ('markitup', 'tests')
DATABASE_ENGINE = 'sqlite3'

try:
    import south
    INSTALLED_APPS += ('south',)
except ImportError:
    pass

MEDIA_URL = '/media/'
MEDIA_ROOT = join(dirname(MIU_TEST_ROOT), 'markitup', 'media')

STATIC_URL = '/static/'
STATIC_ROOT = MEDIA_ROOT

ROOT_URLCONF = 'tests.urls'

MARKITUP_FILTER = ('tests.filter.testfilter', {'arg': 'replacement'})
