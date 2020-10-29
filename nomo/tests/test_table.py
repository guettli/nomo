# Create your tests here.
import os
import unittest

from nomo.table import validate_table_name, drop_table, create_table, drop_column, add_column, list_tables

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django

django.setup()


class Test(unittest.TestCase):
    table_name = 'test_table__should_get_deleted_automatically'
    column_name = 'test_column__should_get_deleted_automatically'


    def test_validate_table_name(self):
        self.assertRaises(ValueError, validate_table_name, 'white space')
        validate_table_name('123-abc_ABC')

    def test_create_table(self):
        drop_table(self.table_name)
        create_table(self.table_name)
        self.assertIn(self.table_name, list_tables())
        self.assertNotIn('auth_user', list_tables())
        drop_table(self.table_name)

    def test_add_column(self):
        drop_table(self.table_name)
        create_table(self.table_name)
        add_column(self.table_name, self.column_name)
        drop_table(self.table_name)
