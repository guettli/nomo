import re
from django.db import connection
from django.urls import reverse
from django.utils.html import format_html
from nomo.utils import fetchall


def create_table(name):
    validate_table_name(name)
    connection.cursor().execute('CREATE table "%s" ()' % name)


def drop_table(name):
    validate_table_name(name)
    connection.cursor().execute('DROP TABLE IF EXISTS "%s"' % name)


table_name_regex = r'^[a-zA-Z0-9_-]+$'


def validate_table_name(name):
    if not re.match(table_name_regex, name):
        raise ValueError('Table name %r does not match Regex %r' % (
            name, table_name_regex))


column_name_regex = r'^[a-zA-Z0-9_-]+$'


def validate_column_name(name):
    if not re.match(column_name_regex, name):
        raise ValueError('Column name %r does not match Regex %r' % (
            name, column_name_regex))


def add_column(table_name, column_name):
    validate_table_name(table_name)
    validate_column_name(column_name)
    connection.cursor().execute('ALTER TABLE "%s" ADD COLUMN "%s" character varying' % (table_name, column_name))


def drop_column(table_name, column_name):
    validate_table_name(table_name)
    validate_column_name(column_name)
    connection.cursor().execute('ALTER TABLE "%s" DROP COLUMN "%s" IF EXISTS' % (table_name, column_name))


tables_to_ignore = set(
    ['django_migrations', 'django_content_type', 'auth_permission', 'auth_group', 'auth_group_permissions',
    'auth_user_groups', 'auth_user_user_permissions', 'auth_user', 'django_session']
)


def list_tables():
    tables = [row[0] for row in
                     fetchall('''select table_name from information_schema.tables where table_schema = 'public' ''') if
    row[0] not in tables_to_ignore]
    return tables

def link_to_table(table_name):
    return format_html('<a href="{}">{}</a>', reverse('table', kwargs=dict(table_name=table_name)), table_name)
