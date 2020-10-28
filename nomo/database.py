import re
from django.db import connection


def create_database(name):
    validate_database_name(name)
    connection.cursor().execute('CREATE DATABASE "%s"' % name)

def drop_database(name):
    validate_database_name(name)
    connection.cursor().execute('DROP DATABASE IF EXISTS "%s"' % name)

database_name_regex = r'^[a-zA-Z0-9_-]+$'
def validate_database_name(name):
    if not re.match(database_name_regex, name):
        raise ValueError('Database name %r does not match Regex %r' % (
            name, database_name_regex))
