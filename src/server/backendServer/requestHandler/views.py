from django.shortcuts import render
from django.http import HttpResponse
from .mock.recognition_mock import *
from requestHandler.models import User
import json

def recognitionRequestHandler(request):
    if request.method == 'GET':
        image = request.FILES
        return HttpResponse(image, content_type="image/jpeg")

        '''
        response = {}
        picture = [2, 3, 4]
        requestedUser = recognitionRequestObject(picture)
        result = recognize(requestedUser)
        response["userId"] = result.userId
        response["song_file_path"] = result.favouriteSongPath
        response["time_processed"] = result.time_recognized
        return HttpResponse(json.dumps(response))
        '''

def requestInfo(request):
    users = User.objects.all()
    result = {}
    for user in users:
        info = {}
        info['firstName'] = user.FirstName
        info['lastName'] = user.LastName
        info['image'] = user.Image.path
        info['FavouriteSongName'] = user.FavouriteSong.SongName
        try:
            info['FavouriteSongPath'] = user.FavouriteSong.File.path
        except:
            info['FavouriteSongPath'] = 'not specified yet'
        result[user.id] = info
    return HttpResponse(json.dumps(result), content_type="application/json")
