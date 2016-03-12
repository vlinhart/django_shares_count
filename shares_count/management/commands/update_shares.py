# -*- coding: utf-8 -*-
from datetime import timedelta, datetime

from django.conf import settings
from django.core.management.base import LabelCommand

from shares_count.models import get_contenttype_model, update_shares

logger = settings.APP_LOGGER


class Command(LabelCommand):
    def handle(self, label, **options):
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

        try:
            sharer_models = getattr(settings, 'SHARER_MODELS')
        except ValueError:
            raise ImproperlyConfigured("SHARER_MODELS must be of the form ['app_label.model_name']")

        for sharer_model in sharer_models:
            app_label, model_name = sharer_model.split('.')
            model, ct = get_contenttype_model(app_label, model_name)
            update_shares(model, ct, age_kwargs=labels_dates[label])
