import cv2
import numpy as np

#img = cv2.imread("C:\\Users\\duttam\\PycharmProjects\\Project_1\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch04\\04_05 Begin\\faces.jpeg",1)

cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    path = "C:\\Users\\duttam\\PycharmProjects\\Project_1\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch04\\04_05 Begin\\haarcascade_frontalface_default.xml"
    # cv2.imshow("Original",gray)
    face_cascade = cv2.CascadeClassifier(path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Image", gray)

    ch = cv2.waitKey(1)
    if ch ==ord('q'):
        break

cap.release()
cv2.distroyAllWindows()

# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# path = "C:\\Users\\duttam\\PycharmProjects\\Project_1\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch04\\04_05 Begin\\haarcascade_frontalface_default.xml"
# #cv2.imshow("Original",gray)
# face_cascade = cv2.CascadeClassifier(path)
# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5,minSize=(40,40))
# for (x,y,w,h) in faces:
#    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()