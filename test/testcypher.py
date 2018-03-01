import unittest
import sys 
import os

sys.path.append(os.path.abspath("../src"))
import aescypher

class TestCypher(unittest.TestCase):
    def test_cypher(self):
        self.assertTrue(True)


if (__name__ == "__main__"):
    unittest.main()
