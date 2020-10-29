from django.urls import path
from nomo.table import table_name_regex

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table/<str:table_name>', views.table, name='table'),
    ]
