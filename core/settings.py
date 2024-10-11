# import os
# from pathlib import Path
# from dotenv import load_dotenv
# from datetime import timedelta


# # load .env file to environment
# load_dotenv()

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-ff(tqdclvi8b@1cx#*^cvoxt@@!())-m3=k&j8+q)^j=74%+q^"

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ["127.0.0.15"]


# # Application definition

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "rest_framework",
#     "rest_framework_simplejwt",
#     "django_filters",
#     "djoser",
#     "drf_spectacular",
#     "authentication",
#     "store",
#     "common",
#     "import_export",
# ]


# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "whitenoise.middleware.WhiteNoiseMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]
# if DEBUG:
#     INSTALLED_APPS += [
#         # "silk",
#         # "debug_toolbar",
#     ]
#     MIDDLEWARE += [
#         # "debug_toolbar.middleware.DebugToolbarMiddleware",
#         # "silk.middleware.SilkyMiddleware",
#     ]

# ROOT_URLCONF = "core.urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = "core.wsgi.application"


# # Database
# # https://docs.djangoproject.com/en/5.1/ref/settings/#databases


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": os.getenv("DBNAME"),
#         "HOST": os.getenv("DBHOST"),
#         "USER": os.getenv("DBUSER"),
#         "PASSWORD": os.getenv("DBPASSWORD"),
#     }
# }


# # Password validation
# # https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/5.1/topics/i18n/

# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static-files")

# MEDIA_URL = "media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# # Default primary key field type
# # https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "localhost"
# EMAIL_PORT = 2525
# EMAIL_HOST_USER = ""  # os.getenv("jo_dev_mail")
# EMAIL_HOST_PASSWORD = ""  # os.getenv("jo_dev_token")
# # EMAIL_USE_TLS = True
# # TAGGIT_CASE_INSENSITIVE = True
# # DEFAULT_FROM_EMAIL = "info@e-market.com"

# INTERNAL_IPS = [
#     # ...
#     "127.0.0.1",
#     # ...
# ]


# REST_FRAMEWORK = {
#     "COERCE_DECIMAL_TO_STRING": False,
#     "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
#     # "PAGE_SIZE": 50,
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     ),
#     "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
# }

# AUTH_USER_MODEL = "authentication.User"

# DJOSER = {
#     "LOGIN_FIELD": "email",
#     "USER_CREATE_PASSWORD_RETYPE": True,
#     "PASSWORD_RESET_CONFIRM_RETYPE": False,
#     "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,  # tell the frontend email not found if it does not exist
#     "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,  # send email when email/username changed
#     "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,  # send email when password changed
#     "SEND_ACTIVATION_EMAIL": True,  # send activation link to the user ,initially account is inactive
#     "SEND_CONFIRMATION_EMAIL": True,  # send when user registration completed and activated
#     "ACTIVATION_URL": "activate/{uid}/{token}",
#     "SERIALIZERS": {
#         "user_create": "authentication.serializers.UserCreateSerializer",
#         "current_user": "authentication.serializers.UserSerializer",
#     },
# }
# SIMPLE_JWT = {
#     "AUTH_HEADER_TYPES": ("JWT",),
#     "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=6),
# }
# SPECTACULAR_SETTINGS = {
#     "TITLE": "e-market api",
#     "DESCRIPTION": "An api for a production level  e-commerce website app ,Yosef.E ",
#     "VERSION": "1.0.0",
#     "SERVE_INCLUDE_SCHEMA": False,
#     # OTHER SETTINGS
# }
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "file": {
#             "level": "ERROR",
#             "class": "logging.FileHandler",
#             "filename": ".log/general.log",
#             "formatter": "verbose",
#         },
#     },
#     "loggers": {
#         "": {
#             "handlers": ["file"],
#             "level": "ERROR",
#             # "propagate": True,
#         },
#     },
#     "formatters": {
#         "verbose": {
#             "format": " {asctime} ({levelname})  {name}  {message}",
#             "style": "{",
#         }
#     },
# }
# # https://docs.python.org/3/library/logging.html#logrecord-attributes
