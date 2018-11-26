###USER should be able to edit password
import webbrowser
import json
import requests

## assume dictionary of password for each user
def getContent(url):
    content = requests.get(url).content
    user_dic = json.loads(content)
    return user_dic

API_url = "http://127.0.0.1:8000/request/"
resoinse_dict = getContent(API_url + "requestLoginInfo")

email = input("please enter your Email:")

if email not in resoinse_dict.keys():
    print("User does not exist try again")
else:
    password = input("Please enter your password:")
    if password == resoinse_dict[email]["passWord"]:
        userId = resoinse_dict[email]["id"]
        url = API_url + "userUpdate?" + "userId=" + str(userId)
        webbrowser.open(url, new=2, autoraise=True)
    else:
        print("incorrect password, please try again")

