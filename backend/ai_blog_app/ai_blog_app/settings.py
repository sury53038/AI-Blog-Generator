"""
Django settings for ai_blog_app project.
"""

from pathlib import Path
import dj_database_url
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&@q1@!xmbcsul#t8!^syaq3u0mubis%nuqa_*w@*nqnbx^%950"

# SECURITY WARNING: don't run with debug turned on in production!
# We check if we are on Render. If yes, turn OFF Debug.
DEBUG = 'RENDER' not in os.environ

# Allow all hosts so Render can access the app
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ai_blog_generator"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", 
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ai_blog_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'], # <--- Fixed syntax slightly
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ai_blog_app.wsgi.application"


# Database
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True 
    )
}
# 'postgresql://neondb_owner:npg_n2RGSU4lrwXW@ep-empty-lake-a1klj9xg-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", },
    { "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    { "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    { "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# This tells Django where to put files when we run 'collectstatic'
STATIC_ROOT = BASE_DIR / "staticfiles"

# This enables Whitenoise to serve the files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


LOGIN_URL = 'login'
