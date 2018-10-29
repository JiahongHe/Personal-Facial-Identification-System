from django.test import TestCase, Client
from requestHandler.models import User, Song
from django.urls import reverse, resolve

class TestRegistration(TestCase):
    # test the registration of the project
    def setUp(self):
        # put some fake song in the test database first
        Song(SongName='Test Song 1').save()
        Song(SongName='Test Song 2').save()
        Song(SongName='Test Song 3').save()
        User(FirstName='Jhon',
             LastName='Doe',
             Gender="('male', 'Male')",
             Image=None,
             FavouriteSong=Song.objects.get(SongName='Test Song 1'),
             Email='validEmail@mail.com').save()
    
    def test_view(self):
        client = Client()
        response_sucess = client.get(reverse('registrationPage'))
        response_failure = client.get('invalidURL')
        self.assertEqual(resolve(reverse('registrationPage')).view_name, 'registrationPage')
        self.assertEqual(response_sucess.status_code, 200)
        self.assertNotEqual(response_failure.status_code, 200)
        

