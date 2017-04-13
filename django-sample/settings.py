import os


ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

DEBUG = os.getenv('DJANGO_SAMPLE_BEBUG')
DJANGO_SAMPLE
ALLOWED_HOSTS = [
    'localhost'
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions'
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.getenv('DJANGO_SAMPLE_DATABASE_HOST'),
        'NAME': os.getenv('DJANGO_SAMPLE_DATABASE_NAME'),
        'USER': os.getenv('DJANGO_SAMPLE_DATABASE_USER'),
        'PASSWORD': os.getenv('DJANGO_SAMPLE_DATABASE_PASSWORD')
    }
}

SESSION_COOKIE_NAME = 'djangosample'
SECRET_KEY = os.getenv('DJANGO_SAMPLE_SECRET_KEY')
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
CSRF_SESSION_NAME = 'csrf'
CSRF_COOKIE_SECURE = True
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

ROOT_URLCONF = 'django-sample.urls'

LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(ROOT_PATH, 'static')
]

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(ROOT_PATH, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.static'
            ]
        }
    }
]