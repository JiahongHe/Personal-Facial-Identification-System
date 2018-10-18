from django.urls import path, include
from . import views


urlpatterns = [
    path('recognitionRequest', views.recognitionRequestHandler, name = "recognit"),
]