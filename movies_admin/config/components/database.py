from environs import Env

env = Env()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB_NAME", default="movies_database"),
        "USER": env.str("POSTGRES_USER", default="app"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", default="123qwe"),
        "HOST": env.str("POSTGRES_HOST", default="127.0.0.1"),
        "PORT": env.int("POSTGRES_PORT", 5432),
    }
}
