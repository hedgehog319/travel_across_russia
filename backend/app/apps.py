from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'
    verbose_name = 'Путешествия'

    def ready(self):
        from app import handlers  # noqa
