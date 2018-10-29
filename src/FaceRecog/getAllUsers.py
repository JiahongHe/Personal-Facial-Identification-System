import requests
import json

def getAllUsers(url):
    content = requests.get(url).content
    user_dic = json.loads(content)
    return user_dic