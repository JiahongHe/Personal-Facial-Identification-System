import unittest
import sys
import requests
sys.path.append('src/FaceRecog/')
sys.path.append('../src/FaceRecog/')
from getAllUsers import getAllUsers

class Test_getAllUsers(unittest.TestCase):

    def setUp(self):

        # change the variale self.url if the server's address changed
        self.url = url = 'http://127.0.0.1:8000/request/requestInfo'

    def test_connectivity(self):

        # test if the server is up and running

        resonse = requests.get(self.url)
        self.assertEqual(resonse.status_code, 200)

    def test_result(self):

        # test if the returned result from the server is as expected.

        result = getAllUsers(self.url)
        self.assertIsInstance(result, dict)
        if len(result) > 0:
            for id, data in result.items():
                self.assertIsInstance(id, str)
                self.assertIsInstance(data, dict)
                self.assertIsInstance(data['firstName'], str)
                self.assertIsInstance(data['lastName'], str)
                self.assertIsInstance(data['image'], str)
                self.assertIsInstance(data['FavouriteSongName'], str)
                self.assertIsInstance(data['FavouriteSongPath'], str)
        
        