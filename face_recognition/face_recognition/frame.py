## detects faces from camera using haarcascade classifications
import cv2
import sys
import os
# CASC_PATH = os.environ['CASC_PATH']

CASC_PATH = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(CASC_PATH)
video_capture = cv2.VideoCapture(0)


path = '/Users/c0l02dy/code/BikeCheck/face_recognition/face_recognition/images'

print(cv2.__version__)

increment = 0
list_images = []
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        print(w,h)
        if w > 250 and h > 250:
            increment = increment + 1  #--- Initiate the increment variable
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            crop_img = frame[y:y+h, x:x+w]
            cv2.imshow("cropped", crop_img)
            list_images.append(crop_img)
            cv2.imwrite(os.path.join(path ,'face' + str(increment) + '.jpg'), crop_img)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
