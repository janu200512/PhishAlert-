import unittest
from utils.helpers import is_suspicious_url

class TestHelpers(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(is_suspicious_url(''), 0.0)
    def test_login(self):
        self.assertGreaterEqual(is_suspicious_url('http://example.com/login'), 0.4)
if __name__ == '__main__':
    unittest.main()
