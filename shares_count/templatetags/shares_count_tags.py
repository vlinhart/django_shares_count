# -*- coding: utf-8 -*-
from django import template
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import register

from shares_count.models import Share

register = template.Library()


@register.filter(is_safe=True)
def share_count(object):
    try:
        return Share.objects.get(
            object_id=object.id, content_type=ContentType.objects.get_for_model(object)
        ).shares
    except Share.DoesNotExist:
        return 0
