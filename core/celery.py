import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


celery = Celery("bg_task")
celery.config_from_object(f"django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()
