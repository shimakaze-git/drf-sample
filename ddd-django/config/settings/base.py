"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*t+##yrkx(i%bjtlk8=!fl7pah7bjqtb!umdn81%)5#+&ei+c('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["localhost", "*"]

URL_ROOT = "/"

# Application definition

INSTALLED_APPS = [
    'django_extensions',
]

INSTALLED_APPS += [
    'django.contrib.admin',  # 管理（admin）サイト
    'django.contrib.auth',  # 認証システム
    'django.contrib.contenttypes',  # コンテンツタイプフレームワーク
    'django.contrib.sessions',  # セッションフレームワーク
    'django.contrib.messages',  # メッセージフレームワーク
    'django.contrib.staticfiles',  # 静的ファイルの管理フレームワーク
    'django.contrib.sites',  # 1つのウェブサイトに1つのSiteデータが割り当て

    # 'polls_app.base_site'
    'polls_app.base_site.apps.BaseSiteConfig',

    # 'polls_app.polls',
    'polls_app.polls.apps.PollsConfig',

    # 'polls_app.user',
    'polls_app.user.apps.UserConfig',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # cache.UpdateCacheMiddleware, cache.FetchFromCacheMiddleware
    # をキャッシュすることで、Djangoプロジェクト全体をキャッシュ


    # 'django.middleware.cache.UpdateCacheMiddleware',  # Cache

    'django.middleware.common.CommonMiddleware',

    # 'django.middleware.cache.FetchFromCacheMiddleware',  # Cache

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [
            os.path.join(BASE_DIR, 'polls_app/templates')
        ],

        'APP_DIRS': True,
        # 'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'config.settings.context_processors.common_variables',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CACHES
CACHES = {
    'default': {
        # Databaseへのキャッシュ
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'polls_app/static')
]


BASE_TITLE = 'shimakaze-git polls'
BASE_DESCRIPTION = ''

SITE_EMAIL = ''
SITE_AUTHOR = 'shimakaze-git'

# サイトマップフレームワークで使う変数
SITE_ID = 1
