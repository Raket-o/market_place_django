# """
# Django settings for market_place project.
#
# Generated by 'django-admin startproject' using Django 5.1.2.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.1/ref/settings/
# """
#
# from pathlib import Path
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-n*n=4ujw-%tpr-*7%woe2bnp9c-*brab9j#bs)wuc5yy6g%myg"
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = []
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
# ]
#
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]
#
# ROOT_URLCONF = "market_place.urls"
#
# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = "market_place.wsgi.application"
#
#
# # Database
# # https://docs.djangoproject.com/en/5.1/ref/settings/#databases
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
#
#
# # Password validation
# # https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/5.1/topics/i18n/
#
# LANGUAGE_CODE = "en-us"
#
# TIME_ZONE = "UTC"
#
# USE_I18N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.1/howto/static-files/
#
# STATIC_URL = "static/"
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



"""
Django settings for market_place project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import logging.config
import os
from pathlib import Path

from django.urls import reverse_lazy

from env_data import db_host, db_name, db_password, db_port, db_user, debug, log_level, url_app


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = debug
DEBUG = os.getenv('DEBUG') != 'False'

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    "192.168.1.125",
    # "172.17.255.255",
    # "10.0.2.255",
    # "10.0.2.2",
    # "10.0.2.15",
    # "192.168.1.1",
    "192.168.55.5",
    url_app,
]

INTERNAL_IPS = [
    "127.0.0.1",
    "0.0.0.0",
    # "192.168.1.125",
    # "172.17.255.255",
    # "10.0.2.255",
    # "10.0.2.2",
    # "10.0.2.15",
    # "192.168.1.1",
    # "czjcaf9can.loclx.io",
]

CSRF_TRUSTED_ORIGINS = [f'https://{url_app}']

if DEBUG:
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS.append("10.0.2.2")
    INTERNAL_IPS.extend(
        [ip[: ip.rfind(".")] + ".1" for ip in ips]
    )


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "debug_toolbar",
    "whitenoise.runserver_nostatic",
    # "phonenumber_field",
    # "rest_framework",
    # "django_filters",
    # "rest_framework.authtoken",
    # "djoser",
    "authorization.apps.AuthorizationConfig",
    "basket.apps.BasketConfig",
    "order.apps.OrderConfig",
    "shop.apps.ShopConfig",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "market_place.urls"

TEMPLATES_PATH = [os.path.join(BASE_DIR, "market_place", "templates/")]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': TEMPLATES_PATH,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "market_place.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
    }
}

# Caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}
CACHE_SECONDS = 60


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "market_place", "templates", "static")]
    MEDIA_URL = "/media/"

else:
    STATIC_ROOT = os.path.join(BASE_DIR, "market_place", "templates", "static")
    MEDIA_URL = STATIC_URL + "media/"
    # MEDIA_URL = "/media/"


# src="/static/media/photo_prod/product_None/photo/ob11.jpg"
# src="/static/media/photo_prod/product_12/photo/ob12_r4h64Mt.jpg"

# src="/static/photo_prod/product_None/photo/ob3.jpeg"
# MEDIA_URL = STATIC_URL + "media/"


# True
# MEDIA_ROOT = BASE_DIR / "uploads"
MEDIA_ROOT = os.path.join(BASE_DIR, "market_place", "templates", "static", "media")



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Django_restframework

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ]
    # 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}


# LOGIN_REDIRECT_URL

LOGIN_REDIRECT_URL = reverse_lazy("shop:top_seller_product")
LOGIN_URL = reverse_lazy("authorization:login")


# Logger

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': log_level,
            'handlers': ['console'],
        },
    },
})