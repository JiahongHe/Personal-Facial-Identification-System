import face_recognition

def get_match(encodings, identities, test_encoding):
    matches = face_recognition.compare_faces(encodings, test_encoding)
    matched_indetity = 'Unknown'
    if True in matches:
        matched_indetity = identities[matches.index(True)]
    return matched_indetity