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
        response = client.get(reverse('register'))
        self.assertEqual(resolve(reverse('register')).view_name, 'register')
        self.assertEqual(response.status_code, 200)
        

