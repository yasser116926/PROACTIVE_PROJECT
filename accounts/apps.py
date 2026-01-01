from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        import accounts.signals
        import accounts.admin
        import accounts.permissions
        import accounts.views
        import accounts.urls
        import accounts.models
        import flights.views
        import flights.urls
        import flights.models
        import flights.admin

from django.contrib.auth import get_user_model                                                                                                                      
