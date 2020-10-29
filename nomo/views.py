from django.http import HttpResponse
from django.utils.html import format_html
from nomo.table import list_tables, link_to_table
from nomo.utils import join


def index(request):
    return HttpResponse(format_html('''
    Hello PostgreSQL
    {}
    ''', join([link_to_table(table_name) for table_name in list_tables()])))


def table(request, table_name):
    assert 0, table_name
