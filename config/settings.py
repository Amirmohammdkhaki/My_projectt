from pathlib import Path
import os
import sys
from environs import Env


env = Env()
env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG", default=True)


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".railway.app",
]


INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "django.contrib.sites",

    "crispy_forms",
    "crispy_bootstrap4",

    "accounts",
    "pages",

    "allauth",
    "allauth.account",
]


SITE_ID = 1


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


TEMPLATES = [

    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

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



# Database PostgreSQL

DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.postgresql",

        "NAME": env("DB_NAME"),

        "USER": env("DB_USER"),

        "PASSWORD": env("DB_PASSWORD"),

        "HOST": env("DB_HOST"),

        "PORT": env.int("DB_PORT"),

    }

}



# Password validation

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },

]



# Authentication

AUTHENTICATION_BACKENDS = [

    "django.contrib.auth.backends.ModelBackend",

    "allauth.account.auth_backends.AuthenticationBackend",

]



AUTH_USER_MODEL = "accounts.CustomUser"



LOGIN_REDIRECT_URL = "home"

LOGOUT_REDIRECT_URL = "home"



# Django Allauth

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_LOGIN_METHODS = {"email"}



# Email Development
# نمایش لینک تایید در ترمینال Docker

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



LANGUAGE_CODE = "en-us"


TIME_ZONE = "UTC"


USE_I18N = True


USE_TZ = True



# Static files

STATIC_URL = "/static/"


STATICFILES_DIRS = [

    os.path.join(BASE_DIR, "static")

]


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# Crispy

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"



# Test database

if "test" in sys.argv:

    DATABASES = {

        "default": {

            "ENGINE": "django.db.backends.sqlite3",

            "NAME": ":memory:",

        }

    }