# -*- coding: utf-8 -*-
from datetime import timedelta, datetime

from django.conf import settings
from django.core.management.base import LabelCommand

from shares_count.models import get_contenttype_model, update_shares

logger = settings.APP_LOGGER


class Command(LabelCommand):
    def handle(self, label, **options):
        model, ct = get_contenttype_model()
        labels_dates = {
            'geront': {'created__lte': datetime.now() - timedelta(days=360)},
            'mature': {
                'created__lte': datetime.now() - timedelta(days=30),
                'created__gt': datetime.now() - timedelta(days=360)
            },
            'teen': {
                'created__lt': datetime.now() - timedelta(days=7),
                'created__gt': datetime.now() - timedelta(days=30)
            },
            'new': {'created__gte': datetime.now() - timedelta(days=7)},
        }
        update_shares(model, ct, age_kwargs=labels_dates[label])
