from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.defUpdatePage, name = "registrationPage"),
    path('update_defaults/', views.updateDefaults, name = "updateDefaults")
]