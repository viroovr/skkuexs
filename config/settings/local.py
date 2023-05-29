from .base import *

ALLOWED_HOSTS = []
BASE_URL = 'http://127.0.0.1:8000/'
INSTALLED_APPS = [
    'common.apps.CommonConfig',
    'skkuexs.apps.SkkuexsConfig',
    'forums.apps.ForumsConfig',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.naver',

    # django-rest-framework
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    # dj-rest-auth
    'dj_rest_auth',
    'dj_rest_auth.registration',

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]