from django.test import TestCase
from requestHandler.models import User, Song
from .test_data import load_test_data

class TestModelUser(TestCase):
    def setUp(self):

        # populate the test database before all the tests
        self.data = load_test_data()
        for _, info in self.data.items():
            User.objects.create(FirstName=info[0], LastName=info[1], Gender=info[2], Email=info[3]).save()
    
    def test_single_User_creation_and_get(self):

        # test single user creation and query functionality

        user1 = User.objects.create(FirstName='Jhon',
                                    LastName='Doe',
                                    Gender="('male', 'Male')",
                                    Email='JohoDoe@test.com')
        user1.save()
        retreived_user1 = User.objects.get(FirstName='Jhon')
        self.assertEqual(retreived_user1.FirstName, user1.FirstName)
        self.assertEqual(retreived_user1.LastName, user1.LastName)
        self.assertEqual(retreived_user1.Gender, user1.Gender)
        self.assertEqual(retreived_user1.Email, user1.Email)
        self.assertEqual(retreived_user1.__str__(), 'Jhon Doe, JohoDoe@test.com')

    def test_User_general(self):

        # A more general test on the database functionalities

        users = User.objects.all()
        self.assertEqual(len(users), len(self.data))
        for i in range(len(users)):
            self.assertEqual(users[i].FirstName, self.data[i][0])
            self.assertEqual(users[i].LastName, self.data[i][1])
            self.assertEqual(users[i].Gender, self.data[i][2])
            self.assertEqual(users[i].Email, self.data[i][3])
            self.assertEqual(users[i].__str__(), self.data[i][0] + ' ' + self.data[i][1] + ', ' + self.data[i][3])

class TestModelSong(TestCase):

    def setUp(self):
        Song(SongName='Test Song 1').save()
        Song(SongName='Test Song 2').save()
        Song(SongName='Test Song 3').save()
        User(FirstName='Jhon',
             LastName='Doe',
             Gender="('male', 'Male')",
             Image=None,
             FavouriteSong=Song.objects.get(SongName='Test Song 1'),
             Email='validEmail@mail.com').save()

    def test_single_song_creation_and_get(self):
        song = Song(SongName='random song')
        song.save()
        song_retrieved = Song.objects.get(SongName='random song')
        self.assertIsInstance(song_retrieved, Song)
        self.assertEqual(song_retrieved.SongName, song.SongName)

    def test_Song_general(self):
        songs = Song.objects.all()
        self.assertEqual(len(songs), 3) # 3 songs reated during setUp
        index = 1
        for song in songs:
            self.assertIsInstance(song, Song)
            self.assertEqual(song.SongName, 'Test Song ' + str(index))
            index += 1
