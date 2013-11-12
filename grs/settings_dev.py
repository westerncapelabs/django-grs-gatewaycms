from settings import *

INTERNAL_IPS = ('127.0.0.1', 'localhost', '::1')

INSTALLED_APPS = INSTALLED_APPS + ('django_extensions', )
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'ENABLE_STACKTRACES': True,
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SKIP_SOUTH_TESTS = True     # Do not run the south tests as part of our
                            # test suite.
SOUTH_TESTS_MIGRATE = False  # Do not run the migrations for our tests.
                             # We are assuming that our models.py are correct
                             # for the tests and as such nothing needs to be
                             # migrated.

FAST_TEST = True

if FAST_TEST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'grs',
            'USER': 'postgres',
    }
}
