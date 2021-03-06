# -*- coding: utf-8 -*-
"""
Django settings for apps project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime
import ldap
from django_auth_ldap.config import LDAPSearch, LDAPSearchUnion, GroupOfNamesType

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',  #配置为先使用LDAP认证，如通过认证则不再使用后面的认证方式
    'django.contrib.auth.backends.ModelBackend',
)
AUTH_LDAP_SERVER_URI = "ldap://ldap.wmq.com:389"  # ldap服务器地址
AUTH_LDAP_BIND_DN = 'cn=manager,dc=wmq,dc=com'  # 管理员账号
AUTH_LDAP_BIND_PASSWORD = 'xxxxx'
OUg = 'DC=wmq,DC=com'
AUTH_LDAP_USER_SEARCH = LDAPSearch(OUg, ldap.SCOPE_SUBTREE, "(&(objectClass=inetOrgPerson)(uid=%(user)s))")
AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn", "alias": "sn", "email": "mail", "username":"name"}
AUTH_LDAP_ALWAYS_UPDATE_USER = True  # 是否同步LDAP修改
AUTH_USER_MODEL = 'account.Users'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mu=5!1$d#nekwavag1h04+5xk96j#2z+)^b9*5aq63-1d2b&uv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'account.apps.AccountConfig',
    'service.apps.ServiceConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'apps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'apps.db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'shutongflow',
        'USER': 'shutongflow',
        'PASSWORD': '123456',
        'PORT': 3306
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'account.ShutongUser'

# JWT
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=12),
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

CORS_ORIGIN_ALLOW_ALL = True

# UEditor settings
UEDITER_SETTING = {
    "fileMaxSize": 10240000,
    "scrawlPathFormat": "",
    "imageUrlPrefix": "",
    "catcherFieldName": "source",
    "snapscreenPathFormat": "",
    "imageFieldName": "upfile",
    "imagePathFormat": "",
    "filePathFormat": "",
    "scrawlMaxSize": 10485760,
    "catcherPathFormat": "",
    "scrawlUrlPrefix": "",
    "videoAllowFiles": [".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg", ".ogg", ".ogv", ".mov", ".wmv",
                        ".mp4", ".webm", ".mp3", ".wav", ".mid"],
    "imageManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "fileManagerListPath": "",
    "imageManagerUrlPrefix": "",
    "scrawlActionName": "uploadscrawl",
    "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "imageManagerListSize": 30,
    "imageManagerActionName": "listimage",
    "videoUrlPrefix": "",
    "fileManagerActionName": "listfile",
    "fileManagerAllowFiles": [".sql", ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".psd.flv", ".swf", ".mkv",
                              ".avi", ".rm", ".rmvb", ".mpeg", ".mpg", ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm",
                              ".mp3", ".wav", ".mid", ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
                              ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml", ".exe",
                              ".com", ".dll", ".msi"],
    "snapscreenUrlPrefix": "",
    "snapscreenActionName": "uploadimage",
    "catcherLocalDomain": ["127.0.0.1", "localhost", "img.baidu.com"],
    "imageActionName": "uploadimage",
    "fileUrlPrefix": "",
    "catcherActionName": "catchimage",
    "imageManagerListPath": "",
    "scrawlFieldName": "upfile",
    "fileManagerUrlPrefix": "",
    "videoActionName": "uploadvideo",
    "fileAllowFiles": [".sql", ".jpg", ".jpeg", ".bmp", ".gif", ".png", ".xls", ".xlsx", ".rar", ".doc", ".docx",
                       ".zip", ".pdf", ".txt", ".swf", ".wmv"],
    "videoPathFormat": "",
    "fileFieldName": "upfile",
    "catcherUrlPrefix": "",
    "catcherMaxSize": 1048576,
    "fileManagerListSize": 30,
    "catcherAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "imageMaxSize": 10485760,
    "videoMaxSize": 10240000,
    "fileActionName": "uploadfile",
    "videoFieldName": "upfile"
}


# the follows should be modify:
WORKFLOWBACKENDURL = "http://0.0.0.0:6060"
WORKFLOWTOKEN = "18070442-276d-11eb-b019-00163e002f56" 
WORKFLOWAPP="ops" 
