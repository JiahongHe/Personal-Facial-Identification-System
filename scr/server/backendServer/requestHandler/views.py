from django.shortcuts import render
from django.http import HttpResponse
from .mock.recognition_mock import *
import json

def recognitionRequestHandler(request):
    response = {}
    picture = [2, 3, 4]
    requestedUser = recognitionRequestObject(picture)
    result = recognize(requestedUser)
    response["userId"] = result.userId
    response["time_processed"] = result.time_recognized
    return HttpResponse(json.dumps(response))