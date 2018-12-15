import face_recognition

def get_match(encodings, identities, test_encoding, ids):
    matches = face_recognition.compare_faces(encodings, test_encoding)
    matched_indetity = 'Unknown'
    matched_id = None
    if True in matches:
        matched_indetity = identities[matches.index(True)]
        matched_id = ids[matches.index(True)]
    return (matched_indetity, matched_id)