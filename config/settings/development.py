"""
Development settings for Tech Service project.
"""
from .base import *  # noqa: F401, F403

# Debug
DEBUG = True

# Email backend (console for development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CORS (if needed for local development)
# CORS_ALLOW_ALL_ORIGINS = True
