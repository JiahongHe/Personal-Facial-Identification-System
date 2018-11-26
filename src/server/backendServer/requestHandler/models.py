from django.db import models
from django.utils import timezone


DEFAULT_PASSWORD = "123456"

class Song(models.Model):

    # models the song that might be used as favourite song for the users.

    SongName = models.CharField(max_length=100)
    File = models.FileField(upload_to='songs/', null=True)
    def __str__(self):
        return self.SongName

class User(models.Model):
    # models the user of this project.

    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    FavouriteSong = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    Email = models.EmailField()
    Image = models.ImageField(upload_to='usersImages/', null=True)
    dateAdded = models.DateTimeField(default=timezone.now)
    passWord = models.CharField(max_length=50, default=DEFAULT_PASSWORD)

    def __str__(self):
	    return "{} {}, {}".format(self.FirstName, self.LastName, self.Email)
