import sys, os

# Ensure the src directory is in the path for imports
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), srcdir)))

import unittest
from src.main import test_function

class TestSum(unittest.TestCase):
    def test_testFunction(self):
        """
        Test that it can sum a list of integers
        """
        self.assertTrue(test_function())

if __name__ == '__main__':
    unittest.main()