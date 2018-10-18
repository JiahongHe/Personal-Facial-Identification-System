from django.db import models
from django.utils import timezone

class Song(models.Model):
    SongName = models.CharField(max_length = 100)
    Album = models.CharField(max_length = 100)
    FilePath = models.CharField(max_length = 100)

    def __str__(self):
        return self.SongName

class User(models.Model):
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Gender = models.CharField(max_length = 10) # to be changed in the future
    FavouriteSong = models.ForeignKey(Song, on_delete = models.CASCADE)
    email = models.EmailField()
    dateAdded = models.DateTimeField(default = timezone.now)

    def __str__(self):
	    return "Name: {} {}, email: {}".format(self.FirstName, self.LastName, self.email)
