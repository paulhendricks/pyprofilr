# pyprofilr/test/test_profile.py

from unittest import TestCase
# import time
import pyprofilr

# ---- Description


class TestProfile(TestCase):
    def test_hello(self):
        self.assertEqual('hello', 'hello')

    def test_is_string(self):
        s = pyprofilr.profile.joke()
        self.assertTrue(isinstance(s, basestring))
