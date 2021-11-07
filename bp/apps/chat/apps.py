from django.apps import AppConfig

# https://django.fun/docs/channels/ru/3/tutorial/part_1/
class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.chat'
