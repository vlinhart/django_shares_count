from __future__ import unicode_literals

import socialshares
import time
from django.apps import apps
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Share(TimeStampedModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    shares = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return '{} {}x'.format(self.content_object, self.shares)

    def update_shares(self):
        orig_shares = self.shares
        self.shares = socialshares.fetch(self.content_object.get_full_url(), ['facebook'], attempts=3).get('facebook',
                                                                                                           0)
        if self.shares != orig_shares:
            self.save()


def get_contenttype_model(app_label, model_name):
    model = apps.get_model(app_label=app_label, model_name=model_name)
    if model is None:
        raise ImproperlyConfigured(
            "%s refers to model '%s' that has not been installed" % app_model_name, app_model_name)
    return model, ContentType.objects.get_for_model(model)


def update_shares(model, content_type, age_kwargs=None, sleep=0.5):
    age_kwargs = age_kwargs or {}
    item_ids = model.objects.filter(**age_kwargs).values_list('id', flat=True).order_by('-created')
    for i, item_id in enumerate(item_ids, start=1):
        share, created = Share.objects.get_or_create(content_type=content_type, object_id=item_id)
        share.update_shares()
        print share
        time.sleep(sleep)
