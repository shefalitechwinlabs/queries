from django.apps import AppConfig


class CrudAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crud_app'

    # Define and import signals
    def ready(self):
        import crud_app.signals
