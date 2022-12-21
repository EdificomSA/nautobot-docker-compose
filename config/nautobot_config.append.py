PLUGINS = ["nautobot_device_onboarding", "nautobot_cable_utils", "nautobot_bulk_connect"]
#"nautobot_version_control"

PLUGINS_CONFIG = {
    'nautobot_bulk_connect': {
        'device_role': None,
    }
}

SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", 'False').lower() == 'true'
SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", 'False').lower() == 'true'
CSRF_COOKIE_SECURE = os.getenv("CSRF_COOKIE_SECURE", 'False').lower() == 'true'

LOGLEVEL = os.getenv('LOGLEVEL', 'INFO')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': LOGLEVEL,
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django_auth_ldap': {
            'handlers': ['console'],
            'level': LOGLEVEL,
        },
    },
}
