from django.db import models
from django.utils import timezone

GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]

class Song(models.Model):
    SongName = models.CharField(max_length = 100)
    Album = models.CharField(max_length = 100)
    File = models.FileField(upload_to = 'songs/', null = True)

    def __str__(self):
        return self.SongName

class User(models.Model):
    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Gender = models.CharField(max_length = 50, choices = GENDER_CHOICES)
    FavouriteSong = models.ForeignKey(Song, on_delete = models.CASCADE, null = True)
    Email = models.EmailField()
    Image = models.ImageField(upload_to = 'usersImages/', blank = True, null = True)
    dateAdded = models.DateTimeField(default = timezone.now)

    def __str__(self):
	    return "{} {}, {}".format(self.FirstName, self.LastName, self.Email)
