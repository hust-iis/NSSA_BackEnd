"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u%gh&47vyr05-@nddy&vy4$mnjx203-nhk%d1bhf%)q2bf1pe1'

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
    'django_crontab',#定时监测，必须要添加到前面，不能接着app后面添加，否则会报错
    # 在此注册各模块的app
    'rest_framework',
    'abnormal_attack',
    'asset_management',
    'risk_analysis',
    'emergency_response',
    'flow_monitoring',
    'incident_response'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 在此注册中间件
]

ROOT_URLCONF = 'web.urls'

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

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nssa-database',
        'USER': 'nssa',
        'PASSWORD': 'c317c317',
        'HOST': '222.20.126.128',
        'PORT': '3366',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#python manage.py crontab add 项目启动时执行，如果已经存在，不用再次执行
#python manage.py crontab remove 项目关闭后执行，不然一直定时检测
CRONJOBS = [
    ('*/2 * * * *', 'flow_monitoring.tasks.set_traffic_value','>>/home/c415/ldf/NSSA_BackEnd/traffic.log'),  # 每2分钟执行一次,日志记录函数打印内容
]

# 发送邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP地址
EMAIL_HOST = 'smtp.qq.com'
# SMTP端口
EMAIL_PORT = 25
# 发送邮箱
EMAIL_HOST_USER = ''
# 发送邮箱授权码，非密码
EMAIL_HOST_PASSWORD = ''

EMAIL_USE_TLS = True  # 是否使用TLS加密

# 添加一个变量，用于存储默认网卡的名称
DEFAULT_NETWORK_INTERFACE = 'eno1'



