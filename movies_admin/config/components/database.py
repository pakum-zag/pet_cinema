import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME') or 'movies_database',
        'USER': os.environ.get('DB_USER') or 'app',
        'PASSWORD': os.environ.get('DB_PASSWORD') or '123qwe',
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}