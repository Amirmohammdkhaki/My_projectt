import os
import sys
from pathlib import Path
from environs import Env

# ==========================
# Environment
# ==========================

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# Security
# ==========================

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".railway.app",
    # ⭐ دامنه شیران — وقتی گرفتی از کامنت درآور
    # "shirangym.ir",
    # "www.shirangym.ir",
]

CSRF_TRUSTED_ORIGINS = [
    "https://*.railway.app",
    # ⭐ دامنه شیران — وقتی گرفتی از کامنت درآور
    # "https://shirangym.ir",
    # "https://www.shirangym.ir",
]

if DEBUG:
    CSRF_TRUSTED_ORIGINS += [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Production Security

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"

# ==========================
# Applications
# ==========================

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
    "products",
    
    "dashboard",

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
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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
# Database
# ==========================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME", default="postgres"),
        "USER": env.str("DB_USER", default="postgres"),
        "PASSWORD": env.str("DB_PASSWORD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.int("DB_PORT", default=5432),
        "CONN_MAX_AGE": 60,
        "OPTIONS": {
            "connect_timeout": 10,
        },
    }
}

# ==========================
# Custom User
# ==========================

AUTH_USER_MODEL = "accounts.CustomUser"

# ==========================
# Password Validation
# ==========================

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

# ⭐ ورود با ایمیل یا نام کاربری
# - کاربر عادی: با ایمیل ثبت‌نام/ورود می‌کند
# - ادمین: با username وارد می‌شود
ACCOUNT_LOGIN_METHODS = {"email", "username"}

# ⭐ در ثبت‌نام: ایمیل + نام کاربری + رمز
# (allauth 65+ الزام می‌کند username در signup باشد اگر در login methods باشد)
ACCOUNT_SIGNUP_FIELDS = [
    "email*",
    "username*",
    "password1*",
    "password2*",
]

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SESSION_REMEMBER = True

# ⭐ تأیید ایمیل اختیاری — برای شروع ساده‌تر
ACCOUNT_EMAIL_VERIFICATION = "optional"

# ⭐ بعد از تأیید ایمیل، کاربر به خانه برود
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "home"

# ⭐ بعد از ورود، اگر ادمین بود به پنل برود (بعداً با signal فعال می‌کنیم)
# LOGIN_REDIRECT_URL = "home"

# ==========================
# Email
# ==========================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# ==========================
# Language & Time
# ==========================

LANGUAGE_CODE = "fa-ir"

TIME_ZONE = "Asia/Tehran"

USE_I18N = True
USE_TZ = True

# ==========================
# Static Files
# ==========================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

if DEBUG:
    STATICFILES_STORAGE_BACKEND = (
        "django.contrib.staticfiles.storage.StaticFilesStorage"
    )
else:
    STATICFILES_STORAGE_BACKEND = (
        "whitenoise.storage.CompressedManifestStaticFilesStorage"
    )

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": STATICFILES_STORAGE_BACKEND,
    },
}

# ==========================
# Media
# ==========================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ==========================
# Default Field
# ==========================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==========================
# Crispy Forms
# ==========================

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# ==========================
# Test Database
# ==========================

if "test" in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    }