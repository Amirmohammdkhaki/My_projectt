from pathlib import Path
import os
import sys
from environs import Env


env = Env()
env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================
# Security
# ==========================

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env.bool(
    "DJANGO_DEBUG",
    default=True
)

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".railway.app",
]


# ==========================
# Applications
# ==========================

INSTALLED_APPS = [

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Sites
    "django.contrib.sites",

    # Third party
    "crispy_forms",
    "crispy_bootstrap4",

    # Local
    "accounts",
    "pages",
    "products",

    # Allauth
    "allauth",
    "allauth.account",
]


SITE_ID = 1


# ==========================
# Middleware
# ==========================

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "allauth.account.middleware.AccountMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "config.urls"


# ==========================
# Templates
# ==========================

TEMPLATES = [

    {
        "BACKEND":
        "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

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


WSGI_APPLICATION = "config.wsgi.application"


# ==========================
# Database PostgreSQL
# ==========================

DATABASES = {

    "default": {

        "ENGINE":
        "django.db.backends.postgresql",

        "NAME":
        env("DB_NAME"),

        "USER":
        env("DB_USER"),

        "PASSWORD":
        env("DB_PASSWORD"),

        "HOST":
        env("DB_HOST"),

        "PORT":
        env.int("DB_PORT"),

    }
}


# ==========================
# Custom User
# ==========================

# accounts/models.py
# class CustomUser(AbstractUser)

AUTH_USER_MODEL = "accounts.CustomUser"


# ==========================
# Authentication
# ==========================

AUTHENTICATION_BACKENDS = [

    "django.contrib.auth.backends.ModelBackend",

    "allauth.account.auth_backends.AuthenticationBackend",

]


LOGIN_REDIRECT_URL = "home"

LOGOUT_REDIRECT_URL = "home"


# ==========================
# Allauth
# ==========================

ACCOUNT_LOGIN_METHODS = {
    "email"
}

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False


ACCOUNT_SIGNUP_FIELDS = [

    "email*",

    "password1*",

    "password2*",

]


ACCOUNT_SESSION_REMEMBER = True


# ==========================
# Email
# ==========================

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)


# ==========================
# Language
# ==========================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ==========================
# Static
# ==========================

STATIC_URL = "/static/"


STATICFILES_DIRS = [

    BASE_DIR / "static"

]


STATIC_ROOT = BASE_DIR / "staticfiles"


STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# ==========================
# Media
# عکس محصولات و کاربران
# ==========================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"



# ==========================
# Default Field
# ==========================

DEFAULT_AUTO_FIELD = (
    "django.db.models.BigAutoField"
)



# ==========================
# Crispy
# ==========================

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"



# ==========================
# Test Database
# ==========================

if "test" in sys.argv:

    DATABASES = {

        "default": {

            "ENGINE":
            "django.db.backends.sqlite3",

            "NAME":
            ":memory:",

        }

    }