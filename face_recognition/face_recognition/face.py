import cognitive_face

KEY = '6621c8d910664c85b1cdea82f8e01f31'  # Replace with a valid Subscription Key here.

########### Python 3.2 #############
import requests
import base64
import json
import numpy as np
from PIL import Image
from io import BytesIO


headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': KEY,
}

params = {
    # Request parameters
    'returnFaceId': True,
    'returnFaceLandmarks': False,
    'returnFaceAttributes': 'gender',
}


url = 'https://eastus2.api.cognitive.microsoft.com/face/v1.0/detect'
payload = {"url": "http://www.gstatic.com/tv/thumb/persons/69735/69735_v9_ba.jpg"}

# print(url)
image_path = '/Users/c0l02dy/code/BikeCheck/face_recognition/face_recognition/images/face18.jpg'

try:
    r = requests.post(url, data=open(image_path, 'rb').read(), params=params, headers=headers)

    data = r.json()
except Exception as e:
    print(e)
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
