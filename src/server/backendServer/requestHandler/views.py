from django.shortcuts import render
from django.http import HttpResponse
from .mock.recognition_mock import *
from requestHandler.models import User
import json

def recognitionRequestHandler(request):

    # handles the face recognition request, currently not in use now, maybe implemented in the future.

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

    # API that returns all the necessary user infomation for facial recognition
    # security measures might be implemented in the future.

    users = User.objects.all()
    result = {}
    for user in users:
        info = {}
        info['firstName'] = user.FirstName
        info['lastName'] = user.LastName
        info['image'] = user.Image.path
        try:
            info['FavouriteSongName'] = user.FavouriteSong.SongName
            info['FavouriteSongPath'] = user.FavouriteSong.File.path
        except Exception as e:
            info['FavouriteSongName'] = 'NULL'
            info['FavouriteSongPath'] = 'NULL'
        result[user.id] = info
    return HttpResponse(json.dumps(result), content_type="application/json")
