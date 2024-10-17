from .common import *
import os

# from pathlib import Path
# from dotenv import load_dotenv
# from datetime import timedelta


load_dotenv()
DEBUG = True
ALLOWED_HOSTS = ["info.jos.com", "192.168.100.43", "127.0.0.1", "172.20.18.55"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DBNAME"),
        "HOST": os.getenv("DBHOST"),
        "USER": os.getenv("DBUSER"),
        "PASSWORD": os.getenv("DBPASSWORD"),
    }
}

INSTALLED_APPS += [
    # "silk",
    "debug_toolbar",
]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "silk.middleware.SilkyMiddleware",
]
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
