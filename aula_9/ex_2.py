
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(
            'lucas'.upper(), 'LUCAS'
        )
    
    def test_isupper(self):
        self.assertTrue('LUCAS'.isupper())
        self.assertFalse('Lucas'.isupper())

if __name__ == '__main__':
    unittest.main()