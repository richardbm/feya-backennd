from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MinistryConfig(AppConfig):
    name = 'ministry'
    verbose_name = _('Ministerio')
