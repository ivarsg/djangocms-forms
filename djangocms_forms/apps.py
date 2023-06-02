# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig
import django
if django.VERSION[0] < 4:
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _


class DjangoCMSFormsConfig(AppConfig):
    name = "djangocms_forms"
    verbose_name = _("Forms")
