import unittest
import face_recognition
import sys
import requests
sys.path.append('src/FaceRecog/')
sys.path.append('../src/FaceRecog/')
sys.path.append('../test/')
from getContent import getContent
from match_face import get_match

def loadTestCase():
    test_pics = []
    test_identites = ['Donald Trump', 'Henry Cavill', 'Barack Obama', 'Unknown', 'Unknown', 'Unknown']
    test_pics.append(face_recognition.load_image_file('test_pics/trump.jpeg'))
    test_pics.append(face_recognition.load_image_file('test_pics/cavill.jpg'))
    test_pics.append(face_recognition.load_image_file('test_pics/obama.jpg'))
    test_pics.append(face_recognition.load_image_file('test_pics/jobs.jpg'))
    test_pics.append(face_recognition.load_image_file('test_pics/gaga.jpg'))
    test_pics.append(face_recognition.load_image_file('test_pics/axl.jpg'))

    return test_pics, test_identites

class Test_FC(unittest.TestCase):

    def setUp(self):

        # change the variale self.url if the server's address changed
        self.url = url = 'http://127.0.0.1:8000/request/requestInfo'

    def test_getMatch(self):

        # test if the match ups are as expected
        user_dic = getContent(self.url)
        encodings = []
        identities = []
        ids = []
        for id, data in user_dic.items():
            image = face_recognition.load_image_file(data['image'])
            encodings.append(face_recognition.face_encodings(image)[0])
            identities.append(data['firstName'] + ' ' + data['lastName'])
            ids.append(id)
            
        test_pics, test_identites = loadTestCase()
        for i, test_pic in enumerate(test_pics):
            face_location = face_recognition.face_locations(test_pic)
            face_encoding = face_recognition.face_encodings(test_pic, face_location)[0]
            matched_identity, id = get_match(encodings, identities, face_encoding, ids)
            self.assertEqual(test_identites[i], matched_identity)
    
