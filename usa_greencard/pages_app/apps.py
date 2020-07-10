from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PagesAppConfig(AppConfig):
    name = 'usa_greencard.pages_app'
    verbose_name = _("PagesApp")

    def ready(self):
        try:
            import usa_greencard.pages_app.signals  # noqa F401
        except ImportError:
            pass
