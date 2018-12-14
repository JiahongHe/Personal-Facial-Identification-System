from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Song)
admin.site.register(SystemSettings)
