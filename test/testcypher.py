import unittest
from src import aescypher
from src import keygenerator

class TestCypher(unittest.TestCase):
    plaintext = "0123456789abcdef".encode()

    def test_encrypt_notEqual(self):
        key = keygenerator.generate()
        cyphertext = aescypher.encrypt(self.plaintext, key)
        self.assertNotEqual(self.plaintext, cyphertext)

    def test_encrypt_ECB(self):
        key = keygenerator.generate()
        cyphertext = aescypher.encrypt(self.plaintext, key, "ECB")
        self.assertNotEqual(self.plaintext, cyphertext)

    def test_encrypt_CBC(self):
        key = keygenerator.generate()
        iv = keygenerator.generate(128)
        cyphertext = aescypher.encrypt(self.plaintext, key, "CBC", iv)
        self.assertNotEqual(self.plaintext, cyphertext)

    def test_encrypt_invalidMode(self):
        key = keygenerator.generate()
        with self.assertRaises(Exception):
            aescypher.encrypt(self.plaintext, key, "TST")

    def test_encrypt_CBC_noIV(self):
        key = keygenerator.generate()
        with self.assertRaises(Exception):
            aescypher.encrypt(self.plaintext, key, "CBC")

    def test_encrypt_key128(self):
        key = keygenerator.generate(128)
        cyphertext = aescypher.encrypt(self.plaintext, key)
        self.assertNotEqual(self.plaintext, cyphertext)

    def test_encrypt_key192(self):
        key = keygenerator.generate(192)
        cyphertext = aescypher.encrypt(self.plaintext, key)
        self.assertNotEqual(self.plaintext, cyphertext)

    def test_encrypt_emptyPlaintext(self):
        key = keygenerator.generate()
        cyphertext = aescypher.encrypt("".encode(), key)
        self.assertNotEqual(self.plaintext, cyphertext)

    def test_encrypt_blockSizeMismtch(self):
        key = keygenerator.generate()
        iv = keygenerator.generate(128)
        plaintext = "test".encode()
        cyphertext = aescypher.encrypt(plaintext, key, "CBC", iv)
        self.assertNotEqual(plaintext, cyphertext)


    def test_decrypt_ECB(self):
        key = keygenerator.generate()
        cyphertext = aescypher.encrypt(self.plaintext, key)        
        res = aescypher.decrypt(cyphertext, key)
        self.assertEqual(self.plaintext, res)
    
    def test_decrypt_CBC(self):
        key = keygenerator.generate()
        iv = keygenerator.generate(128)
        cyphertext = aescypher.encrypt(self.plaintext, key, "CBC", iv)        
        res = aescypher.decrypt(cyphertext, key, "CBC", iv)
        self.assertEqual(self.plaintext, res)

    def test_decrypt_invalidKey(self):
        key = keygenerator.generate()
        cyphertext = aescypher.encrypt(self.plaintext, key)

        invalid_key = keygenerator.generate()
        while (invalid_key == key):
            invalid_key = keygenerator.generate()
        
        res = aescypher.decrypt(cyphertext, invalid_key)
        self.assertNotEqual(self.plaintext, res)

    def test_decrypt_modeMismatch(self):
        key = keygenerator.generate()
        iv = keygenerator.generate(128)
        cyphertext = aescypher.encrypt(self.plaintext, key, "CBC", iv)        
        res = aescypher.decrypt(cyphertext, key, "ECB")
        self.assertNotEqual(self.plaintext, res)

    def test_decrypt_invalidMode(self):
        key = keygenerator.generate()
        cyphertext = aescypher.encrypt(self.plaintext, key) 
        with self.assertRaises(Exception):
            aescypher.decrypt(cyphertext, key, "TST")

    def test_decrypt_key128(self):
        key = keygenerator.generate(128)
        cyphertext = aescypher.encrypt(self.plaintext, key)        
        res = aescypher.decrypt(cyphertext, key)
        self.assertEqual(self.plaintext, res)

    def test_decrypt_key192(self):
        key = keygenerator.generate(192)
        cyphertext = aescypher.encrypt(self.plaintext, key)        
        res = aescypher.decrypt(cyphertext, key)
        self.assertEqual(self.plaintext, res)

    def test_decrypt_emptyPlaintext(self):
        key = keygenerator.generate()
        plaintext = "".encode()
        cyphertext = aescypher.encrypt(plaintext, key)
        res = aescypher.decrypt(cyphertext, key)
        self.assertEqual(plaintext, res)

    def test_decrypt_char(self):
        key = keygenerator.generate()
        plaintext = "a".encode()
        cyphertext = aescypher.encrypt(plaintext, key)
        res = aescypher.decrypt(cyphertext, key)
        self.assertEqual(plaintext, res)



if (__name__ == "__main__"):
    unittest.main()
