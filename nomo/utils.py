from django.db import connection
from django.utils.html import format_html_join, format_html


def execute(sql, data=None):
    cursor = connection.cursor()
    cursor.execute(sql, data)
    return cursor

def fetchall(sql, data=None):
    return execute(sql, data).fetchall()

def join(my_list):
    if not my_list:
        return ''
    return format_html('<ul>{}</ul>', format_html_join('\n', "<li>{}</li>", [[item] for item in my_list]))