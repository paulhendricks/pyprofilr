# pyprofilr/test/test_profile.py

from unittest import TestCase
# import time
from pyprofilr import *
from pyprofilr.profile import joke

# ---- Description


class TestProfile(TestCase):
    def test_hello(self):
        self.assertEqual('hello', 'hello')

    def test_is_string(self):
        s = joke()
        self.assertTrue(isinstance(s, basestring))

    def test_is_also_string(self):
        p = profile()
        self.assertTrue(isinstance(p, basestring))

    def test_should_break(self):
        self.assertEqual('hello world', 'hello world')
