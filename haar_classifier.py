import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("C:\\Users\\duttam\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\data\\haarcascade_frontalface_alt2.xml")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors= 5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        cv2.rectangle(frame,(x,y),(x+h,y+w),(255,0,0),4)
    cv2.imshow("Frame",frame)
    ch = cv2.waitKey(1)
    if ch == ord('q'):
        break

cap.relase()
cv2.destroyAllWindows()



