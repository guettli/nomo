# Create your tests here.
import os
import unittest

from nomo.table import validate_table_name, drop_table, create_table

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django

django.setup()


class Test(unittest.TestCase):
    def test_validate_table_name(self):
        self.assertRaises(ValueError, validate_table_name, 'white space')
        validate_table_name('123-abc_ABC')

    def test_create_table(self):
        name = 'test_table__should_get_deleted_automatically'
        drop_table(name)
        create_table(name)
        drop_table(name)
