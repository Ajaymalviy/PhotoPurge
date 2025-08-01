"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--86oenvzrsktb1^m$w+f85we_z%#hc-kk9#-__h_)l0e&0h$q+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #my apps
    'gmailapp',
    'photos',
    #allauth
    "allauth_ui",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    "widget_tweaks",
    "slippers",
    #https for local development
    'sslserver',

]
SOCIALACCOUNT_STORE_TOKENS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Must be before custom middleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'gmailapp.middleware.TokenRefreshMiddleware',
]

ROOT_URLCONF = 'codegeeks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
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

WSGI_APPLICATION = 'codegeeks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gmail',
        'USER': 'ajay',
        'PASSWORD': 'Root@123',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}



SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email', 'https://mail.google.com/',  'https://www.googleapis.com/auth/photoslibrary'],
        'AUTH_PARAMS': {
            'access_type': 'offline',
            'prompt' : 'consent' 
        },
        'OAUTH_PKCE_ENABLED': True,
        'APP': {
              'client_id': '99034799467-hl9dbl4t4l64gftesd8bokb1no6kbgu3.apps.googleusercontent.com',
              'secret': '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',
            # for local development
            #'client_id': '99034799467-6l1lm0l6b80h2bcmon2i8st2odg778nj.apps.googleusercontent.com',
            #'secret': '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',
            'key': ''
        }
    }   
    
}


LOGIN_REDIRECT_URL = '/'
# LOGIN_REDIRECT_URL = '/'  # Redirect after successful login
LOGOUT_REDIRECT_URL = '/' 



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # For regular Django authentication
    'allauth.account.auth_backends.AuthenticationBackend',  # For allauth authentication
)

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
#celery configrations :
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE =False
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

#configuration for celery redis message queue working in background for executing tasks defined in tasks module of both apps
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # URL for Redis
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 43200


CSRF_TRUSTED_ORIGINS = [
    'https://del.codemos.in',
]

#smtp configurations
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'codegeek004@gmail.com'
EMAIL_HOST_PASSWORD = 'tljz zgdr rwwt cpva' 

EMAIL_PORT = 587


ALLAUTH_UI_THEME = "light"

#custom user model
AUTH_USER_MODEL = 'gmailapp.CustomUser'


