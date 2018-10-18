import datetime

class recognitionRequestObject:
    def __init__(self, picture):
        self.picture = picture
        self.time_created = datetime.datetime.now()

class recognizedUser:
    def __init__(self, userId):
        self.userId = userId
        self.time_recognized = str(datetime.datetime.now())

def recognize(to_recognize):
    result = recognizedUser(userId = "randomUser")
    return result