from environs import Env

env = Env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME', default='movies_database'),
        'USER': env.str('DB_USER', default='app'),
        'PASSWORD': env.str('DB_PASSWORD', default='123qwe'),
        'HOST': env.str('DB_HOST', default='127.0.0.1'),
        'PORT': env.int('DB_PORT', 5432),
    }
}