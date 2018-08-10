import cv2
import sys
import os
import requests

video_capture = cv2.VideoCapture(0)

class Face(object):

    def __init__(self, image_path="./current_face.jpg"):
        self.frame = None
        self.face = None
        self.image_path = image_path


    def grab_frame(self):
        frame = None
        print(video_capture.isOpened())
        if not video_capture.isOpened():
            video_capture.open()
        ret, frame = video_capture.read()
        print(frame)
        frame_detected = frame
        self.frame = frame
        print("writing to fs")
        cv2.imwrite(self.image_path, self.frame)
        video_capture.release()
        print(dir(video_capture))
        print(type(video_capture.release))

    def detect_users(self):
        #r = requests.post(face_url, data=open(self.image_path, 'rb').read(), params={}, headers={})
        # return (r.status_code  == 200, r.json())
        return True, [{'name':'bo', 'dimensions':[100,200,300,400]}]

    def find_user(self, user):
        print(user)
        #user == {'name':'joe', 'dimensions':[2,3,100,100]}
        # Draw a rectangle around the faces
        x, y, w, h = user['dimensions']
        cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        self.face = self.frame[y:y+h, x:x+w]
        cv2.imwrite(self.image_path, self.face)
        return self.face
