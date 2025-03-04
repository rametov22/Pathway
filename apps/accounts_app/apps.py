from django.apps import AppConfig


class AccountsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts_app"

    def ready(self):
        import apps.accounts_app.signals
