# Create your tests here.
import os
import unittest

from nomo.table import validate_table_name, drop_table, create_table, drop_column, add_column, list_tables
from nomo.utils import join

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django

django.setup()


class Test(unittest.TestCase):
    def test_join(self):
        self.assertEqual('<ul><li>ab</li>\n<li>&lt;&gt;</li>\n<li>&amp;</li></ul>', join(['ab', '<>', '&']))
        self.assertEqual('', join([]))