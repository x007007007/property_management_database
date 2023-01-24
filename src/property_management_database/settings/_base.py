from ._env import *

INSTALLED_APPS = [
    *([
          # 'grappelli.dashboard',
          'grappelli',
      ] if ENABLE_GRAPPELLI else []),
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    # admin enhance
    'rangefilter',
    'django_admin_listfilter_dropdown',
    'django_extensions',
    'rest_framework',
    'graphene_django',
    'guardian',
    'property_management_database.app.goods',
    'property_management_database.app.hub',
    'property_management_database.app.menu',
    'property_management_database.app.payment.alipay',
    'property_management_database.app.graphql',
    'property_management_database.app.rbac',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'
