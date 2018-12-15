from django.db import models
from django.utils import timezone


DEFAULT_PASSWORD = "123456"
DEFAULT_BEHAVIOR_CHOICES = (
    ("RandomSong", "RandomSong"),
    ("DefaultSong", "DefaultSong"),
    ("Voice", "Voice"),
)

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
    FavouriteSong = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    Email = models.EmailField()
    Image = models.ImageField(upload_to='usersImages/', null=True)
    dateAdded = models.DateTimeField(default=timezone.now)
    passWord = models.CharField(max_length=50, default=DEFAULT_PASSWORD)

    def __str__(self):
	    return "{} {}, {}".format(self.FirstName, self.LastName, self.Email)

    def voice_welcome_line(self):
        return "welcome, {}".format(self.FirstName)

class SystemSetting(models.Model):
    DefaultBehavior = models.CharField(max_length=50,
                                        choices=DEFAULT_BEHAVIOR_CHOICES,
                                        default="DefaultSong")
    DefaultSong = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True)

    def save(self):
        count = SystemSetting.objects.all().count()
        save_permission = SystemSettings.has_add_permission(self)

        # if there's more than two objects it will not save them in the database
        if count >= 1:
            SystemSetting.objects.all().delete()
        super(SystemSetting, self).save()
            
            

    def has_add_permission(self):
        return not SystemSetting.objects.exists()
    
    def __str__(self):
        return "DefaultBehavior: {}".format(self.DefaultBehavior)