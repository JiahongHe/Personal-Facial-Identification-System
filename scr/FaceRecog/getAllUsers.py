import requests
import json

def getAllUsers():
    content = requests.get('http://127.0.0.1:8000/request/requestInfo').content
    user_dic = json.loads(content)
    return user_dic