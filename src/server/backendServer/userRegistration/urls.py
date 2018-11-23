from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.registrationPage, name = "registrationPage"),
    path('register/', views.register, name = "register"),
    path('update_defaults/', views.update_defaults, name = "update_defaults")
]