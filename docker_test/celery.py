import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docker_test.settings")
app = Celery("dotest")
app.config_from_object("django.conf:settings", namespace="CELERY")

from celery.signals import setup_logging

@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig
    from django.conf import settings
    dictConfig(settings.LOGGING)

app.autodiscover_tasks()