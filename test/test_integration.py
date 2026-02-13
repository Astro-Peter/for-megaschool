import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest

# There's nothing here yet!

from httpx import Client
from src.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = Client(app=app)

    def test_root(self):
        response = self.client.get('/')
        assert response.status_code == 200
