from django.apps import AppConfig


class EditorConfig(AppConfig):
    name = 'editor'
    verbose_name = 'Editor Config File'

    def ready(self):
        from . import signals

