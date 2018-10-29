import cv2
import face_recognition
from getAllUsers import getAllUsers

if __name__ == '__main__':

    # main function for the facial recognition system 
    # to make it work:
    # 1. make sure the server is runing, if the address of the server is not 'http://127.0.0.1:8000/'
    #    change the variable API_url below to the correct server address.
    # 2. run this script.

    print('retrieving all user data from the server')
    API_url = 'http://127.0.0.1:8000/request/requestInfo'
    user_dic = None
    try:
        print('Data received, starting facial recognition..')
        user_dic = getAllUsers(API_url)
    except:
        raise ConnectionError('can not connect to the server to retreive user data')
    encodings = []
    identities = []
    for id, data in user_dic.items():
        print(data['image'])
        image = face_recognition.load_image_file(data['image'])
        encodings.append(face_recognition.face_encodings(image)[0])
        identities.append(data['firstName'] + ' ' + data['lastName'])

    cv2.namedWindow("preview")
    video_capture = cv2.VideoCapture(0)

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face enqcodings in the frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(encodings, face_encoding)

            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = identities[first_match_index]

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()