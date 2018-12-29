from django.contrib import admin
from requestHandler.models import User, Song, SystemSetting

admin.site.register(User)
admin.site.register(Song)
admin.site.register(SystemSetting)
