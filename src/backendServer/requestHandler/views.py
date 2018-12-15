from django.shortcuts import render
from django.http import HttpResponse
from requestHandler.models import User, Song, SystemSetting
from .forms import updateForm
import json

fields = ['FirstName',
         'LastName',
         'Email',
         'passWord']

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
        result[user.FirstName + user.LastName] = info
    return HttpResponse(json.dumps(result), content_type="application/json")

def requestLoginInfo(request):
    # API that returns all the necessary user infomation for user login

    users = User.objects.all()
    result = {}
    for user in users:
        info = {}
        info['Email'] = user.Email
        info['passWord'] = user.passWord
        info['id'] = user.id
        result[user.Email] = info
        
    return HttpResponse(json.dumps(result), content_type="application/json")

def requestUpdateUserInfo(request):
    if request.method == 'GET':
        userId = request.GET["userId"]
        user = User.objects.get(id=userId)
        
        initials = {}
        for field in fields:
            initials[field] = user.__dict__[field]
        initials['FavouriteSong'] = user.FavouriteSong
        initials['Image'] = user.Image
        initials['userId'] = user.id
        initials['passWord'] = user.passWord
        form = updateForm(initial=initials)
        form.fields['Email'].widget.attrs['readonly'] = True
        context = {"form": form}
        return render(request, "requestHandler/updateInfo.html", context)

    elif request.method == 'POST':
        form = updateForm(request.POST, request.FILES)
        if form.is_valid():
            userId = form.cleaned_data['userId']
            user = User.objects.get(id=userId)
            if user is not None:
                for field in fields:
                    user.__dict__[field] = form.cleaned_data[field]
                user.save()
                return HttpResponse("update saved!")
            else:
                return HttpResponse("user not found")
        else:
            return HttpResponse("invalid information")

def getSettings(request):
    if request.method == 'GET':
        settingObj = SystemSetting.objects.all()
        result = {}
        if (len(settingObj) > 0):
            setting = settingObj[0]
            result["defaultBehavior"] = setting.DefaultBehavior
            result["defaultSong"] = setting.DefaultSong.SongName if setting.DefaultSong is not None else "Null"
            return HttpResponse(json.dumps(result), content_type="application/json")
        else:
            result["defaultBehavior"] = "Null"
            result["defaultSong"] = "NULL"
            return HttpResponse(json.dumps(result), content_type="application/json")

def getSongs(request):
    if request.method == 'GET':
        result = {}
        Songs = Song.objects.all()
        for song in Songs:
            result[song.SongName] = song.File.path if song.File is not None else "None"
        return HttpResponse(json.dumps(result), content_type="application/json")


