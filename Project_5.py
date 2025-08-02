# FACE DETECTION AND RECOGNITION
#  Develop an AI application that can detect and recognize faces in
#  images or videos. Use pre-trained face detection models like Haar
#  cascades or deep learning-based face detectors, and optionally
#  add face recognition capabilities using techniques like Siamese
#  networks or ArcFace

import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('image.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

resize_img = cv2.resize(img,(800,600))

cv2.imshow('Face detection',resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()