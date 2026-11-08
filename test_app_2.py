import unittest
from app import app

class TestApp2(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_unknown_route(self):
        response = self.client.get('/page-inexistante')
        self.assertEqual(response.status_code, 404)

    def test_sum_negative(self):
        response = self.client.post('/sum', data={'a': '-2', 'b': '5'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'3.0', response.data)

    def test_sum_decimal(self):
        response = self.client.post('/sum', data={'a': '2.5', 'b': '1.5'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'4.0', response.data)

    def test_hello_spaces_only(self):
        response = self.client.post('/hello', data={'username': '   '})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello there', response.data)

if __name__ == "__main__":
    unittest.main()
