import re
import psycopg2

def create_database(name):
    from django.db import connection
    validate_database_name(name)
    connection.cursor().execute('CREATE DATABASE "%s"' % name)

database_name_regex = r'^[a-zA-Z0-9_-]+$'
def validate_database_name(name):
    if not re.match(database_name_regex, name):
        raise ValueError('Database name %r does not match Regex %r' % (
            name, database_name_regex))
