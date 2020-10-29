# Create your tests here.
import os
import unittest

from nomo.database import validate_database_name, create_database, drop_database

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()


class Test(unittest.TestCase):
    def test_validate_database_name(self):
        self.assertRaises(ValueError, validate_database_name, 'white space')
        validate_database_name('123-abc_ABC')

    def test_create_database(self):
        name = 'test_database__should_get_deleted_automatically'
        drop_database(name)
        create_database(name)
        drop_database(name)

