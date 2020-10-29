import re
from django.db import connection


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
