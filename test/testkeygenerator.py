import unittest
from src import keygenerator

class TestKeyGenerator(unittest.TestCase):
    def test_generate_zero(self):
        with self.assertRaises(Exception):
            keygenerator.generate(0)

    def test_generate_noparam(self):
        self.assertEqual(len(keygenerator.generate()), 32)

    def test_generate_128(self):
        self.assertEqual(len(keygenerator.generate(128)), 16)

    def test_generate_192(self):
        self.assertEqual(len(keygenerator.generate(192)), 24)

    def test_generate_256(self):
        self.assertEqual(len(keygenerator.generate(256)), 32)


if (__name__ == "__main__"):
    unittest.main()

