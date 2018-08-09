import cv2
import sys
import os
import requests

class Face(object):

    def __init__(self, image_path="face.jpg"):
        self.frame = None
        self.face = None
        self.image_path = image_path


    def grab_frame(self):
        frame_detected = False
        while not frame_detected:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_detected = True
            self.frame = frame
            cv2.imwrite(self.image_path, self.frame)

            video_capture.release()

    def detect_users(self):

        r = requests.post(face_url, data=open(self.image_path, 'rb').read(), params={}, headers={})
        return (r.status_code  == 200, r.json())


    def find_user(self, user):
        #user == {'dimensions':[2,3,100,100]}

        # Draw a rectangle around the faces
        for (x, y, w, h) in user['dimensions']:
            cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            self.face = self.frame[y:y+h, x:x+w]
        return cropped_img
