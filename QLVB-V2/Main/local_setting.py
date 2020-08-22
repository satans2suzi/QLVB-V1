ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = []

TIME_ZONE = 'Asia/Ho_Chi_Minh'

DATETIME_INPUT_FORMATS = "%Y-%m-%d %H:%M:%S"

USE_L10N = False

USE_TZ = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testprogram',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
