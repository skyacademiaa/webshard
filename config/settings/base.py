"""
Base settings for Tech Service project.
Common settings shared between development and production.
"""
import os
from pathlib import Path
import environ

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Environment
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ['localhost', '127.0.0.1']),
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Security
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default=['*'])
CSRF_TRUSTED_ORIGINS = [
    'https://*.liara.run',
    'http://*.liara.run',
    'https://tech-service.liara.run',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]


# ──────────────────────────────────────────────
# Application definition
# ──────────────────────────────────────────────

DJANGO_APPS = [
    'jazzmin',  # Must be before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'crispy_tailwind',
    'taggit',
    'imagekit',
]

LOCAL_APPS = [
    'apps.core',
    'apps.services',
    'apps.portfolio',
    'apps.pricing',
    'apps.blog',
    'apps.about',
    'apps.contact',
    'apps.quote',
    'apps.seo',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# ──────────────────────────────────────────────
# Middleware
# ──────────────────────────────────────────────

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'


# ──────────────────────────────────────────────
# Templates
# ──────────────────────────────────────────────

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.core.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# ──────────────────────────────────────────────
# Database
# ──────────────────────────────────────────────

DATABASES = {
    'default': env.db('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
}


# ──────────────────────────────────────────────
# Password validation
# ──────────────────────────────────────────────

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ──────────────────────────────────────────────
# Internationalization (Persian RTL)
# ──────────────────────────────────────────────

LANGUAGE_CODE = 'fa'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('fa', 'فارسی'),
    ('en', 'English'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# ──────────────────────────────────────────────
# Static files
# ──────────────────────────────────────────────

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ──────────────────────────────────────────────
# Media files
# ──────────────────────────────────────────────

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ──────────────────────────────────────────────
# Default primary key field type
# ──────────────────────────────────────────────

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ──────────────────────────────────────────────
# Crispy Forms (Tailwind)
# ──────────────────────────────────────────────

CRISPY_ALLOWED_TEMPLATE_PACKS = 'tailwind'
CRISPY_TEMPLATE_PACK = 'tailwind'


# ──────────────────────────────────────────────
# Taggit
# ──────────────────────────────────────────────

TAGGIT_CASE_INSENSITIVE = True


# ──────────────────────────────────────────────
# Jazzmin Admin Theme
# ──────────────────────────────────────────────

JAZZMIN_SETTINGS = {
    'site_title': 'پنل مدیریت',
    'site_header': 'Tech Service',
    'site_brand': 'Tech Service',
    'welcome_sign': 'به پنل مدیریت خوش آمدید',
    'copyright': 'Tech Service',
    'search_model': ['blog.Article', 'portfolio.Project'],
    'topmenu_links': [
        {'name': 'مشاهده سایت', 'url': '/', 'new_window': True},
    ],
    'show_sidebar': True,
    'navigation_expanded': True,
    'icons': {
        'core.SiteSettings': 'fas fa-cog',
        'core.Slider': 'fas fa-images',
        'core.Testimonial': 'fas fa-quote-right',
        'services.Service': 'fas fa-concierge-bell',
        'portfolio.Project': 'fas fa-briefcase',
        'portfolio.ProjectCategory': 'fas fa-folder',
        'pricing.PricingCategory': 'fas fa-tags',
        'pricing.PricingModule': 'fas fa-puzzle-piece',
        'blog.Article': 'fas fa-newspaper',
        'blog.ArticleCategory': 'fas fa-bookmark',
        'about.TeamMember': 'fas fa-users',
        'contact.ContactMessage': 'fas fa-envelope',
        'quote.ProjectQuote': 'fas fa-file-invoice',
    },
    'custom_css': 'css/admin_custom.css',
    'custom_js': None,
    'use_google_fonts_cdn': True,
    'show_ui_builder': False,
}

JAZZMIN_UI_TWEAKS = {
    'theme': 'darkly',
    'dark_mode_theme': 'darkly',
}
