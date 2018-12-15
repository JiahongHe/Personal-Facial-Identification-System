from django.urls import path, include
from . import views


urlpatterns = [
    path('requestInfo', views.requestInfo, name='test'),
    path('requestLoginInfo', views.requestLoginInfo, name='requestLoginInfo'),
    path('userUpdate', views.requestUpdateUserInfo, name='userUpdate'),
    path('getSettings', views.getSettings, name='getSettings'),
    path('getSongs', views.getSongs, name='getSongs'),
]