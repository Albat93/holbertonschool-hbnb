import unittest
import requests

class TestAdminAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000/admin'

    def test_get_admin(self):
        response = requests.get(f'{self.base_url}/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('admin', response.json())

    def test_create_admin(self):
        response = requests.post(self.base_url, json={'name': 'New Admin'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())

    def test_update_admin(self):
        response = requests.put(f'{self.base_url}/1', json={'name': 'Updated Admin'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Updated Admin')

    def test_delete_admin(self):
        response = requests.delete(f'{self.base_url}/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()