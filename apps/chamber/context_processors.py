# -- coding: utf-8 --
from django.conf import settings


def coffee42test_settings_context(request):
    return {'coffe42cups_settings': settings}
