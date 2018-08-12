import cv2
import sys
import os
import requests

FACE_URL = 'https://test-crud.azurewebsites.net'
# FACE_URL = 'https://eastus2.api.cognitive.microsoft.com/face/v1.0/detect'
# FACE_HEADERS = {
#     'Ocp-Apim-Subscription-Key': '6621c8d910664c85b1cdea82f8e01f31',
#     'Content-Type': 'application/octet-stream'}
# FACE_PARAMS = {'returnFaceId': True,
#     'returnFaceLandmarks': False,
#     'returnFaceAttributes': 'gender',}
class Face(object):
    video_capture = cv2.VideoCapture(0)

    def __init__(self, image_path="./current_face.jpg"):
        self.frame = None
        self.face = None
        self.image_path = image_path
        self.face_id = None

    def grab_frame(self):
        frame = None
        ret, frame = Face.video_capture.read()
        frame_detected = frame
        self.frame = frame
        cv2.imwrite(self.image_path, self.frame)

    def detect_users(self):
        detect_resp = requests.post(FACE_URL + "/detect_face", data=open(self.image_path, 'rb').read())#, params=FACE_PARAMS, headers=FACE_HEADERS)
        print('----DETECT FACE----')
        print(detect_resp.status_code)
        print(detect_resp.json())
        print('-------------------')
        if detect_resp.status_code == 200:
            user_data = detect_resp.json()
            self.face_id = user_data.get('faceId')
            print("checking if face is a user")
            face_resp = requests.post(FACE_URL + "/face_is_user", data={'face_id': self.face_id})
            f_data = face_resp.json()
            print('face_resp: ', f_data)
            if f_data.get('found') == 'true':
                print("found user! ", {**f_data, **detect_resp.json()})
                return True, {**f_data, **detect_resp.json()}
        return False, None

    def find_user(self, user):
        print(user)
        #user == {'name':'joe', 'dimensions':[2,3,100,100]}
        # Draw a rectangle around the faces
        y, x, w, h = user['faceRectangle'].values()
        cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        self.face = self.frame[y:y+h, x:x+w]
        cv2.imwrite(self.image_path, self.frame)
        return self.face
