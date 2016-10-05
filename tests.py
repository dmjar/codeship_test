import requests
import unittest

class TestStringMethods(unittest.TestCase):
    def test_must_return_hello_world(self):
        r = requests.get('http://127.0.0.1:5000')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, 'Hello World!')
