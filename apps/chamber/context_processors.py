# -- coding: utf-8 --
from django.conf import settings


def coffee42test_settings_context(request):
    return {'coffee42test_settings': settings}
