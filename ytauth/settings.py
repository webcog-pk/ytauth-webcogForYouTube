import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d(8j@m*k_eex1z1og--ok7yy&(%%8_31__ewvk!n7d0!*wy1!u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    'core',
    'widget_tweaks',

    'allauth',
    'allauth.account',

    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

    'allauth.mfa',

    'django.contrib.humanize',
    'allauth.usersessions',
]

SITE_ID=1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "allauth.account.middleware.AccountMiddleware",
    'allauth.usersessions.middleware.UserSessionsMiddleware',

]


ROOT_URLCONF = 'ytauth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ytauth.wsgi.application'

ACCOUNT_FORMS = {
    'signup':'core.forms.CustomSignupForm',
}
AUTH_USER_MODEL = 'core.CustomProfiles'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'core.backends.EmailOrUsernameModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

    # pairs
    # username + password
    # email + password
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     "/var/www/static/",
# ]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# emailsneidnconfi
# google

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yourmail@gmail.com'
EMAIL_HOST_PASSWORD = 'yourapppassword'
# app password
# ALLAUTHSETTINS

LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED=True #recommended
# ACCOUNT_CHANGE_EMAIL=False
# ACCOUNT_MAX_EMAIL_ADDRESSES = 6
ACCOUNT_CHANGE_EMAIL=True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1
ACCOUNT_EMAIL_NOTIFICATIONS=True
ACCOUNT_EMAIL_VERIFICATION="mandatory" #recommend
ACCOUNT_LOGIN_BY_CODE_ENABLED=True
ACCOUNT_LOGIN_BY_CODE_MAX_ATTEMPTS=4
ACCOUNT_LOGIN_BY_CODE_TIMEOUT = 120
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION=False
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE=True
ACCOUNT_LOGIN_ON_PASSWORD_RESET=False
LOGOUT_REDIRECT_URL="/"
ACCOUNT_SESSION_REMEMBER=False
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE=False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE=True
ACCOUNT_USERNAME_BLACKLIST = ['admin','webcog','youtube']
ACCOUNT_UNIQUE_EMAIL=True #recommended
ACCOUNT_USERNAME_MIN_LENGTH=4
ACCOUNT_USERNAME_REQUIRED=True




SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    },
     'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
        "VERIFIED_EMAIL": True,
    },
}
