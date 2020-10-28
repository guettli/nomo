from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.urls import reverse


class NoMoConfig(AppConfig):
    name = 'nomo'

