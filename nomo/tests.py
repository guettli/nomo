# Create your tests here.
import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()


from django.urls import reverse

from django.test import Client



