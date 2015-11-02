# pyprofilr/test/profile.py

import unittest
import time
from ..import *

# ---- Description

class TestProfile(unittest.TestCase):
    def test_hello(self):
        self.assertEqual('hello', 'hello')