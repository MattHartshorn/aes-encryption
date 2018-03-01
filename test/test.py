import unittest
from testcypher import TestCypher
from testkeygenerator import TestKeyGenerator

if __name__ == '__main__':
    # Specify test classes
    tests = [TestKeyGenerator, TestCypher]

    # Load tests 
    loader = unittest.TestLoader()
    suite = [loader.loadTestsFromTestCase(test) for test in tests]
    runnable_suite = unittest.TestSuite(suite)

    # Run
    results = unittest.TextTestRunner().run(runnable_suite)