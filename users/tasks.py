import logging
import datetime
from django.db.models import Q
from django.utils import timezone

from celery import shared_task


log = logging.getLogger(__name__)


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={'max_retries': 5})
def send_dispute_email_task(self):
    print(*range(1, 1001))
