import requests
import json

def getContent(url):
    content = requests.get(url).content
    user_dic = json.loads(content)
    return user_dic