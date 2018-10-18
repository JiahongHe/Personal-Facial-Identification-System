from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('request/', include('requestHandler.urls')),
    path('registration/', include('userRegistration.urls')),
]
